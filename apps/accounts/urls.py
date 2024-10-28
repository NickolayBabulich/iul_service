from django.urls import path

from apps.accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # Форма авторизации
    path('signin/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        extra_context={'page_title': 'Авторизация'},
    ),
         name='login'),
    # Форма регистрации
    path('signup/', views.SignUpView.as_view(
        extra_context={'page_title': 'Создание аккаунта'}
    ),
         name='signup'),
    # Форма восстановления пароля
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password/password_reset_form.html',
             email_template_name='accounts/password/password_reset_email.html',
             subject_template_name='accounts/password/password_reset_subject.txt',
             success_url='/auth/password-reset/done/',
             extra_context={'page_title': 'Восстановление пароля'}
         ),
         name='password_reset'),
    # Форма подтверждения отправки информации по восстановлению пароля
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password/password_reset_done.html',
             extra_context={'page_title': 'Восстановление пароля'}
         ),
         name='password_reset_done'),
    # Форма установки нового пароля
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password/password_reset_confirm.html',
             success_url='/auth/password-reset-complete/',
             extra_context={'page_title': 'Установка нового пароля'}
         ),
         name='password_reset_confirm'),
    # Форма подтверждения изменения пароля
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password/password_reset_complete.html',
             extra_context={'page_title': 'Пароль изменен'}
         ),
         name='password_reset_complete'),
    path('signup/done/', views.SignUpDoneView.as_view(), name='signup-done'),
    path('signup/confirm/', views.SignUpConfirmView.as_view(), name='signup-confirm'),

]
