from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, ProfileForm
from .models import CustomUser


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountLogoutView(LogoutView):
    pass


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.display_name = user.get_full_name() or user.username
            user.save(update_fields=('display_name',))
            login(request, user)
            messages.success(request, 'Your account was created successfully.')
            return redirect('accounts:dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.role == CustomUser.Role.ADMIN or request.user.is_superuser:
        return render(request, 'accounts/admin_dashboard.html')
    return render(request, 'accounts/member_dashboard.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
