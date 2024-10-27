from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts.forms import CustomUserCreationForm

# class Login(LoginView):
#     success_url = reverse_lazy('signup')
#     template_name = 'accounts/login.html'

# class PasswordReset(PasswordResetView):
#     success_url = reverse_lazy('signup')
#     template_name = 'registration/password_reset_form.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'accounts/signup.html'
