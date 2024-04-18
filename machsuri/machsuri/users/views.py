from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import views as auth_views

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user directly after registration
            return redirect('home')  # Redirect to a home or dashboard page
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')  # Redirect to a home or dashboard page
                else:
                    return render(request, 'users/login.html', {'form': form, 'error': 'Your account is disabled.'})
            else:
                return render(request, 'users/login.html', {'form': form, 'error': 'Invalid login details.'})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
    
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'users/password_change_form.html'
    success_url = '/users/password_change/done/'

class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'

class PasswordReset(auth_views.PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = '/users/password_reset/done/'

class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = '/users/reset/done/'

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'