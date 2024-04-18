from django.urls import path
from .views import register, user_login, user_logout, profile, PasswordChange, PasswordChangeDone, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete


urlpatterns = [
    path('register/', register, name='register'),  # User registration
    path('login/', user_login, name='login'),  # User login
    path('logout/', user_logout, name='logout'),  # User logout
    path('profile/', profile, name='profile'),  # User profile
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetComplete.as_view(), name='password_reset_complete'),
]