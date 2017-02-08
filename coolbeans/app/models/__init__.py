from django.db.models import DateTimeField
from django.db.models import Model

# Discoverable model imports
from coolbeans.app.models.user import UserModel

class TimeStampedModel(Model):
    """
    An abstract base class model that provides self-managed "created_at" and "modified" fields.
    """

    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


