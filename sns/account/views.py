from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from .forms import AccountSiginupForm
from .models import Account

# Create your views here.
class AccountSignUpView(generic.CreateView):
    form_class = AccountSiginupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class AccountLoginView(auth_views.LoginView):
    template_name = 'account/login.html'

class AccountLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'

class AccountDetailView(generic.DetailView):
    model = Account
    template_name = 'account/detail.html'
