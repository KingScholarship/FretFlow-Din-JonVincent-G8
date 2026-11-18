from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegistrationForm
from .models import Profile


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountLogoutView(LogoutView):
    pass


def register(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(
                user=user,
                defaults={'display_name': user.get_full_name() or user.username},
            )
            login(request, user)
            messages.success(request, 'Your account was created successfully.')
            return redirect('accounts:dashboard')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={'display_name': request.user.get_full_name() or request.user.username},
    )
    if profile.role == Profile.Role.ADMIN or request.user.is_superuser:
        return render(request, 'accounts/admin_dashboard.html', {'profile': profile})
    return render(request, 'accounts/member_dashboard.html', {'profile': profile})


@login_required
def profile(request):
    member_profile, _ = Profile.objects.get_or_create(
        user=request.user,
        defaults={'display_name': request.user.get_full_name() or request.user.username},
    )
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=member_profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=member_profile, user=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
