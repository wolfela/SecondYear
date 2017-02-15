from django.db.models import CASCADE
from django.db.models import CharField, PositiveIntegerField, BooleanField, TextField
from django.db.models import ForeignKey
from django_mysql.models import ListCharField
from model_utils.managers import InheritanceManager
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin

from coolbeans.app.models.base import TimeStampedModel
from coolbeans.app.models.quiz import QuizModel


class QuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A base model for a Question.
    """
    _safedelete_policy = SOFT_DELETE

    quiz = ForeignKey(QuizModel, on_delete=CASCADE)
    parent = ForeignKey('self', on_delete=CASCADE)
    display_order = PositiveIntegerField()

    objects = InheritanceManager()

    def check_answer(self, answer):
        """
        Checks whether the supplied answer is correct.

        :param answer: The answer provided.
        :return: bool Whether the answer is correct.
        """
        raise NotImplementedError()


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
    question = ForeignKey(QuestionModel, on_delete=CASCADE)
    answers = ListCharField(base_field = CharField(max_length=255, blank = False))
    correct = CharField(max_length=255, blank = False)
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


class TFQuestionModel(QuestionModel):
    """
    A True or False Question Type.
    """
    question = ForeignKey(QuestionModel, on_delete=CASCADE)
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
