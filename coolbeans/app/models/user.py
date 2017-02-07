from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import EmailField, CharField
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteMixin

from coolbeans.app.models import TimeStampedModel


class User(AbstractBaseUser, TimeStampedModel, SafeDeleteMixin):
    _safedelete_policy = SOFT_DELETE

    email = EmailField(max_length=200, unique=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name
