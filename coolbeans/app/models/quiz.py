from django.db import models
from django.db.models import ListCharField, CharField, TextField, DateTimeField
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

    language = CharField(max_length=255)
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    questions = ListCharField(max_length=255, base_field=CharField(max_length=255, blank=True, null=True), blank=True)