from django.db.models import Model, DateTimeField


class TimeStampedModel(Model):
    """
    An abstract base class model that provides self-managed "created_at" and "modified" fields.
    """

    created_at = DateTimeField(auto_now_add=True,blank=True)
    modified_at = DateTimeField(auto_now=True,blank=True)

    class Meta:
        abstract = True