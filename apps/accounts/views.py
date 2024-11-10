from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.tokens import default_token_generator

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView
from django.views.generic.base import View
from apps.accounts.forms import CustomUserCreationForm
from apps.accounts.utils import send_verification_email


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:signup_done')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        send_verification_email(self.request, user)

        return response

class SignUpDoneView(TemplateView):
    template_name = 'accounts/signup_done.html'

class SignUpConfirmView(TemplateView):
    template_name = 'accounts/signup_confirm.html'


class EmailVerificationView(View):
    def get(self, request, uidb64, token):
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            print(f"Debug - decoded uid: {uid}")

            user = User.objects.get(pk=uid)

            if not user.is_active and default_token_generator.check_token(user, token):
                print("Debug - Activating user...")
                user.is_active = True
                user.save()

                user.refresh_from_db()

                login(request, user)

                messages.success(request, 'Ваш email успешно подтвержден!')
                return redirect('accounts:signup_confirm')
            else:
                if user.is_active:
                    messages.info(request, 'Ваш аккаунт уже активирован.')
                    return render(request, 'accounts/email_verification_error.html')
                else:

                    messages.error(request, 'Ссылка для активации недействительна!')
                    user.delete()

                return render(request, 'accounts/email_verification_error.html')

        except (TypeError, ValueError, OverflowError):
            messages.error(request, 'Ошибка при обработке ссылки активации.')
            return redirect('accounts:signup')

        except User.DoesNotExist:

            messages.error(request, 'Пользователь не найден.')
            return redirect('accounts:signup')