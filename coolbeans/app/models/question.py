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



class BaseQuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A base model for a Question.
    """

    _safedelete_policy = SOFT_DELETE
    display_with = ForeignKey('self', on_delete=CASCADE, blank=True, null=True)
    display_order = PositiveIntegerField(blank=True, default=1)

    objects = InheritanceManager()

    def check_answer(self, answer):
        """
        Checks whether the supplied answer is correct.

        :param answer: The answer provided.
        :return: bool Whether the answer is correct.
        """
        all = self.crosswordquestionmodel_set.all()

        for element in answer['data']:
            for obj in all:
                if(obj.x==element['x'] and obj.y==element['y']):
                    if(element['answer']==obj.answer):
                        break;
                    else:
                        return False

        return True

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
    score = PositiveIntegerField(blank=True, default=0, null=True)
    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)

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

    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)

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


class WordMatchingModel(BaseQuestionModel):
    """
    A Word Matching Question Type.
    """
    title = CharField(max_length=500, blank=True)
    score = PositiveIntegerField(blank=True, default=1, null=True)
    listA = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False), blank=True)
    listB = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False), blank=True)
    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)

    class Meta:
        verbose_name = "Word Matching Question"
        verbose_name_plural = "Word Matching Questions"

    def check_answer(self, answerA, answerB):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided.
        :return: bool Whether the answer is correct.
        """
        if(len(answerA)<len(self.listA) or len(answerB)<len(self.listB)):
            return False


        i=0
        for a in answerA:
            j = 0
            for b in self.listA:
                if(b==a):
                    if(self.listB[j]==answerB[i]):
                        break;
                    else:
                        return False
                j=j+1
            i=i+1


        return True


class WordScrambleQuestionModel(BaseQuestionModel):
    """
    A Word Scrabble Question Type.
    """
    title = CharField(max_length=500)
    answer = CharField(max_length=255)
    scrambled_sentence = CharField(max_length=500, blank = False)
    score = PositiveIntegerField(blank=True, default=1, null=True)
    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)
    class Meta:
        verbose_name = "Word Scramble Question"
        verbose_name_plural = "Word Scramble Questions"

    def check_answer(self, choice):
        """
        Checks whether the supplied answer is correct.

        :param choice: The answer provided
        :return: bool Whether the answer is correct.
        """

        return choice == self.answer.split(" ")


class GapFillQuestionModel(BaseQuestionModel):
    """
    A Question Type for gap fill type questions.
    """

    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)
    question = CharField(max_length=500, blank=False)
    gaps = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False), blank=True)


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
    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)

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
            "clue": self.clue,
            "answer": self.answer,
            "pos": self.position,
            "quiz": self.quiz
}