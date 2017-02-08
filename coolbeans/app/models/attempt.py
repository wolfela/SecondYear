from django.db.models import CASCADE
from django.db.models import ForeignKey
from safedelete.models import SafeDeleteMixin

from coolbeans.app.models.quiz import QuizModel
from coolbeans.app.models.user import UserModel
from coolbeans.app.models.base import TimeStampedModel


class AttemptModel(TimeStampedModel, SafeDeleteMixin):
    """
    A model for an attempt of a quiz.
    """
    user_id = ForeignKey(UserModel, on_delete=CASCADE)
    quiz_id = ForeignKey(QuizModel, on_delete=CASCADE)