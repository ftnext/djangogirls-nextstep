from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),
    path('password_change/', views.PasswordChange.as_view(),
         name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(),
         name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(),
         name='password_reset_done'),
]
