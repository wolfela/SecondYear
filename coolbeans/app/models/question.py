from django.db.models import CASCADE
from django.db.models import CharField, PositiveIntegerField
from django.db.models import ForeignKey
from django_mysql.models import ListCharField
from model_utils.managers import InheritanceManager
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin
from coolbeans.app.models.base import TimeStampedModel


class BaseQuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A base model for a Question that stores quiz id and position in the quiz for each question.
    """

    _safedelete_policy = SOFT_DELETE
    quiz = CharField(max_length=500, blank=False, default="0")
    position = CharField(max_length=500, blank=False, default="0")

    objects = InheritanceManager()

    def check_answer(self, answer):
        """
        Checks whether the supplied crossword answer is correct

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

class MultipleChoiceModel(BaseQuestionModel):
    """
    An MC Question Type. It stores an array of all answers and seperately the correct answer.
    """
    title = CharField(max_length=500, blank=False)
    answers = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=True, null=True), blank=True)
    correct = CharField(max_length=255, blank=False)


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


class WordMatchingModel(BaseQuestionModel):
    """
    A Word Matching Question Type. It stores two arrays of corresponding values.
    """
    title = CharField(max_length=500, blank=True)
    listA = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False), blank=True)
    listB = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False), blank=True)

    class Meta:
        verbose_name = "Word Matching Question"
        verbose_name_plural = "Word Matching Questions"

    def check_answer(self, answerA, answerB):
        """
        Checks whether the supplied answer is correct.
        :param answerA: list of left values
        :param answerB: list of corresponding right values
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
    A Word Scrabble Question Type. It stores an answer sentence.
    """
    title = CharField(max_length=500)
    answer = CharField(max_length=500)

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
    A Question Type for gap fill type questions. Stores the whole questions and a list of gap words.
    """

    question = CharField(max_length=500, blank=False)
    gaps = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=False), blank=True)

    def check_answer(self, answers):
        """
        Checks whether the supplied answer is correct.
        :param answers: The answers provided
        :return: bool Whether the answer is correct.
        """
        return answers == self.gaps


class CrosswordQuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A Crossword Entry Question Type. Stores base question as Foreign Key.
    One entry holds one word, its direction, starting coordinates (x,y) and clue
    """
    question = ForeignKey(BaseQuestionModel, on_delete=CASCADE, blank=True, null=True)
    direction = CharField(max_length=500)
    length = PositiveIntegerField()
    x = PositiveIntegerField()
    y = PositiveIntegerField()
    clue = CharField(max_length=500)
    answer = CharField(max_length=500)
    quiz = CharField(max_length=500, blank=False)
    position = CharField(max_length=500, blank=False)

    class Meta:
        verbose_name = "Crossword Question"
        verbose_name_plural = "Crossword Questions"

    def as_dict(self):
        """
        Method for retrieving the data from the database as a dict
        :return: dict with selected fields
        """
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