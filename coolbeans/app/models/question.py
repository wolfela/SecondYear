from django.db.models import CASCADE
from django.db.models import CharField, PositiveIntegerField
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

    title = CharField(max_length=255)
    quiz = ForeignKey(QuizModel, on_delete=CASCADE)
    parent = ForeignKey('self', on_delete=CASCADE)
    display_order = PositiveIntegerField()

    objects = InheritanceManager()


class MCQQuestionModel(QuestionModel):
    """
    An MCQ Question Type.
    """
    pass