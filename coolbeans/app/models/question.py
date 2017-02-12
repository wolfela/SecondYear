from django.db.models import CASCADE
from django.db.models import CharField, PositiveIntegerField, BooleanField
from django.db.models import ForeignKey
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


class MCQQuestionModel(QuestionModel):
    """
    An MCQ Question Type.
    """
    task = "Choose a correct answer" #default task info for each question type, just an idea I'm not sure if we need it
    question = ForeignKey(QuestionModel, on_delete=CASCADE)
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
        answer = Answer.objects.get(id=choice)

        if answer.correct is True:
            return True
        else:
            return False

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in
                Answer.objects.filter(mcq = self)]



class Answer(TimeStampedModel, SafeDeleteMixin):
    """
    Answer type for MCQ question
    """
    mcq = ForeignKey(MCQQuestionModel, on_delete=CASCADE)
    content  = CharField(max_length=255, blank = False)
    correct = BooleanField(blank = False)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"