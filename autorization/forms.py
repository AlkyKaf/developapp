from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# User = get_user_model()


class UserCreationForms(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
