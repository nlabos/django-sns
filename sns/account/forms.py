from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Account
class AccountSiginupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountSiginupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Account
        fields = ("username", "password1", "password2", )

class AccountLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    class Meta:
        model = Account
        fields = ("username", "password", )
