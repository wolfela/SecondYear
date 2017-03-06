from django.db.models import CASCADE
from django.db.models import ForeignKey
from django_mysql.models import DynamicField
from safedelete.models import SafeDeleteMixin

from coolbeans.app.models.base import TimeStampedModel
from coolbeans.app.models.question import BaseQuestionModel
from coolbeans.app.models.quiz import QuizModel
from coolbeans.app.models.user import UserModel


class AttemptModel(TimeStampedModel, SafeDeleteMixin):
    """
    A model for an attempt of a quiz.
    """
    user_id = ForeignKey(UserModel, on_delete=CASCADE)
    quiz_id = ForeignKey(QuizModel, on_delete=CASCADE)


class AttemptQuestionModel(TimeStampedModel, SafeDeleteMixin):
    """
    A model for storing an attempt for a question.
    """
    attempt_id = ForeignKey(AttemptModel, on_delete=CASCADE)
    question_id = ForeignKey(BaseQuestionModel, on_delete=CASCADE)
    data = DynamicField()