from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import EmailField, CharField


class User(AbstractBaseUser):
    email = EmailField(max_length=200, unique=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    