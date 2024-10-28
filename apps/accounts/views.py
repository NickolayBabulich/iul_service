from django.contrib.auth.views import LoginView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from apps.accounts.forms import CustomUserCreationForm

# class Login(LoginView):
#     success_url = reverse_lazy('signup')
#     template_name = 'accounts/login.html'

# class PasswordReset(PasswordResetView):
#     success_url = reverse_lazy('signup')
#     template_name = 'registration/password_reset_form.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:signup-done')
    template_name = 'accounts/signup.html'

class SignUpDoneView(TemplateView):
    template_name = 'accounts/signup_done.html'

class SignUpConfirmView(TemplateView):
    template_name = 'accounts/signup_confirm.html'
