import json
from json.decoder import JSONDecodeError

from bs4 import BeautifulSoup
from django.db.models import CASCADE
from django.db.models import CharField, PositiveIntegerField, BooleanField, TextField
from django.db.models import ForeignKey, Model
from django_bleach.models import BleachField
from django_mysql.models import ListCharField
from jsonschema import ValidationError
from jsonschema import validate
from model_utils.managers import InheritanceManager
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin
from django.core.exceptions import ObjectDoesNotExist
import random

from coolbeans.app.exceptions import HTMLParseError
from coolbeans.app.models.base import TimeStampedModel
from coolbeans.app.models.quiz import QuizModel



class BaseQuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A base model for a Question.
    """

    _safedelete_policy = SOFT_DELETE

    quiz = ForeignKey(QuizModel, on_delete=CASCADE, blank=True, null=True)
    display_with = ForeignKey('self', on_delete=CASCADE, blank=True, null=True)
    display_order = PositiveIntegerField(blank=True, default=1)

    objects = InheritanceManager()

    def check_answer(self, answer):
        """
        Checks whether the supplied answer is correct.

        :param answer: The answer provided.
        :return: bool Whether the answer is correct.
        """
        raise NotImplementedError()

    def get_children(self):
        """
        Returns all the questions that are displayed together
        :return: all the questions displayed together
        """

        return BaseQuestionModel.objects.filter(display_with = self)



class PlaceholderQuestionModel(BaseQuestionModel):
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


class MultipleChoiceModel(BaseQuestionModel):
    """
    An MCQ Question Type.
    """
    title = CharField(max_length=500, blank=False)
    answers = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=True, null=True), blank=True)
    correct = CharField(max_length=255, blank=False)
    score = PositiveIntegerField(blank=True, default=1, null=True)

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
        return self.answers.extend(self.correct) #TO DO: sort out display order+{anws


class WordMatchingQuestionModel(BaseQuestionModel):
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
            pair = Pair.objects.filter(question=self).get(left_value=choice)
        except ObjectDoesNotExist:
            print("Wrong entry or choice does not exist")
            raise

        return pair.right_value == answer


class Pair(TimeStampedModel, SafeDeleteMixin):
    """
    A pair value for a word matching question type
    """
    question = ForeignKey(WordMatchingQuestionModel, on_delete=CASCADE)
    left_value = CharField(max_length=500, blank=False)
    right_value = CharField(max_length=500, blank = False)


class WordScrambleQuestionModel(BaseQuestionModel):
    """
    A Word Scrabble Question Type.
    """
    title = CharField(max_length=500)
    answer = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False))
    scrambled_sentence = CharField(max_length=500, blank = False)
    score = PositiveIntegerField(blank=True, default=1, null=True)

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


class GapFillQuestionModel(BaseQuestionModel):
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


class CrosswordQuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A Word Scrabble Question Type.
    """
    question = ForeignKey(BaseQuestionModel, on_delete=CASCADE, blank=True, null=True)
    direction = CharField(max_length=500)
    length = PositiveIntegerField()
    x = PositiveIntegerField()
    y = PositiveIntegerField()
    clue = CharField(max_length=500)
    score = PositiveIntegerField(blank=True, default=1, null=True)
    answer = CharField(max_length=500)

    class Meta:
        verbose_name = "Crossword Question"
        verbose_name_plural = "Crossword Questions"

    def check_answer(self, choice):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided
        :return: bool Whether the answer is correct.
        """

        return choice==self.answer

    def as_dict(self):
        return {
            "direction": self.direction,
            "length": self.length,
            "x": self.x,
            "y": self.y,
            "clue": self.clue
        }