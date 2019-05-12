from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:post_list'),
         name='logout'),
    path('password_change/', views.PasswordChange.as_view(),
         name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(),
         name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(),
         name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetComplete.as_view(),
         name='password_reset_complete'),
]
