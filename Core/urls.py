from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.edit_profile, name='profile'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # path('activate_email/<email_token>', views.activate_email, name='activate_email'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="authentication/registration/password_reset_form.html"),name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="authentication/registration/password_reset_done.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="authentication/registration/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="authentication/registration/password_reset_complete.html"),name='password_reset_complete'),
]
