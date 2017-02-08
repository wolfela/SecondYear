from django.db import models
from django.db.models import CharField, TextField, DateTimeField
from django.db.models import ForeignKey
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin

from coolbeans.app.models.base import TimeStampedModel
from coolbeans.app.models.user import UserModel


class QuizModel(TimeStampedModel, SafeDeleteMixin):
    """
    A model for a quiz.
    """
    _safedelete_policy = SOFT_DELETE

    slug = CharField(max_length=100)
    title = CharField(max_length=255)
    description = TextField(blank=True, null=True)
    creator = ForeignKey(UserModel, on_delete=models.DO_NOTHING)