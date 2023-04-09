from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None


class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password',]
        help_text = {'username': None}