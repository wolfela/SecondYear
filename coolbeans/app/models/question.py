import json
from json.decoder import JSONDecodeError

from bs4 import BeautifulSoup
from django.db.models import CASCADE
from django.db.models import CharField, PositiveIntegerField, BooleanField, TextField
from django.db.models import ForeignKey
from django_bleach.models import BleachField
from django_mysql.models import ListCharField
from jsonschema import ValidationError
from jsonschema import validate
from model_utils.managers import InheritanceManager
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin
from django.core.exceptions import ObjectDoesNotExist

from coolbeans.app.exceptions import HTMLParseError
from coolbeans.app.models.base import TimeStampedModel
from coolbeans.app.models.quiz import QuizModel


class QuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A base model for a Question.
    """
    _safedelete_policy = SOFT_DELETE

    quiz = ForeignKey(QuizModel, on_delete=CASCADE)
    display_with = ForeignKey('self', on_delete=CASCADE)
    display_order = PositiveIntegerField()

    objects = InheritanceManager()

    def check_answer(self, answer):
        """
        Checks whether the supplied answer is correct.

        :param answer: The answer provided.
        :return: bool Whether the answer is correct.
        """
        raise NotImplementedError()

    def get_the_group(self):
        """
        Returns all the questions that are displayed together
        :return: all the questions displayed together
        """

        return QuestionModel.objects.filter(display_with = self)


class PlaceholderQuestionModel(QuestionModel):
    """
    A question model for placeholder information.
    """
    information = TextField()


    def check_answer(self, answer):
        """
        Checks whether the supplied answer is correct.

        :param answer: The answer provided.
        :return: bool Whether the answer is correct.
        """
        return None # undefined behaviour

class MCQQuestionModel(QuestionModel):
    """
    An MCQ Question Type.
    """
    title = CharField(max_length=500, blank=False)
    answers = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False))
    correct = CharField(max_length=255, blank=False)
    score = PositiveIntegerField()

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"

    def check_answer(self, choice):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided.
        :return: bool Whether the answer is correct.
        """

        return self.correct == choice

    def get_answers_list(self):
        return self.answers.extend(self.correct) #TO DO: sort out display order


class TrueFalseQuestionModel(QuestionModel):
    """
    A True or False Question Type.
    """
    title = CharField(max_length=500)
    answer = BooleanField(blank=False)
    score = PositiveIntegerField()

    class Meta:
        verbose_name = "True or False Question"
        verbose_name_plural = "True or False Questions"

    def check_answer(self, choice):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided.
        :return: bool Whether the answer is correct.
        """

        return self.answer is choice


class WordMatchingQuestionModel(QuestionModel):
    """
    A Word Matching Question Type.
    """
    title = CharField(max_length=500)
    score = PositiveIntegerField()

    class Meta:
        verbose_name = "Word Matching Question"
        verbose_name_plural = "Word Matching Questions"

    def check_answer(self, choice, answer):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided in "left | right" format
        :return: bool Whether the answer is correct.
        """
        try:
            pair= Pair.objects.filter(question = self).get(left_value=choice)
        except ObjectDoesNotExist:
            print("Wrong entry or choice does not exist")

        return pair.right_value == answer


class Pair(TimeStampedModel, SafeDeleteMixin):
    """
    A pair value for a word matching question type
    """
    question = ForeignKey(WordMatchingQuestionModel, on_delete=CASCADE)
    left_value = CharField(max_length=500, blank=False)
    right_value = CharField(max_length=500, blank = False)



class WordScrambleQuestionModel(QuestionModel):
    """
    A Word Scrable Question Type.
    """
    title = CharField(max_length=500)
    answer = CharField(max_length=500, blank = False)
    scrambled_sentence = CharField(max_length=500, blank = False)
    score = PositiveIntegerField()

    class Meta:
        verbose_name = "Word Scramble Question"
        verbose_name_plural = "Word Scramble Questions"

    def check_answer(self, choice):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided
        :return: bool Whether the answer is correct.
        """

        return choice==self.answer


class GapFillQuestionModel(QuestionModel):
    """
    A Question Type for gap fill type questions.
    """

    # Gap schema: <gap answers='["answer1", "answer2"]' />
    text = BleachField(allowed_tags=["gap"], allowed_attributes=["answers"])
    gap_tag_schema = {
        "type": "array",
        "items": {
            "type": "string"
        }
    }

    def _clean_fields(self):
        super().clean_fields()

    # TODO This should be a view method
    def check_html(self, html):
        """
        Checks if the HTML fragment can be accepted. Validates all <gap> tags to see if they conform to the standard.
        :param html:
        :return:
        """
        bs = BeautifulSoup(html, 'html.parser')
        for tag in bs.find_all('gap'):
            if not tag.has_attr('answers'):
                raise HTMLParseError("One of the gaps is missing an 'answers' attribute")
            try:
                validate(json.loads(tag['answers']), self.gap_tag_schema)
            except (JSONDecodeError, ValidationError) as e:
                raise HTMLParseError("Gap JSON parsing failed: Invalid syntax") from e
        return True
