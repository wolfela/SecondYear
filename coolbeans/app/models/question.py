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

    class Meta:
        abstract = True


class MCQQuestionModel(QuestionModel):
    """
    An MCQ Question Type.
    """
    task = "Choose a correct answer" #default task info for each question type, just an idea I'm not sure if we need it
    question = ForeignKey(QuestionModel, on_delete=CASCADE)
    score = PositiveIntegerField()

    def check_if_correct(self, choice):
        answer = Answer.objects.get(id = choice)

        if answer.correct is True:
            return True
        else:
            return False

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in
                Answer.objects.filter(mcq = self)]

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"


class Answer(TimeStampedModel, SafeDeleteMixin):
    """
    Answer type for MCQ question
    """
    mcq = ForeignKey(MCQQuestionModel, on_delete=CASCADE)
    content  = CharField(max_length=255, blank = False)
    correct = BooleanField(blank = False, deafult = False)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"