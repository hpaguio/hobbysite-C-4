from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def profile_view(request):
    """
    Displays the logged-in user's profile information.
    """
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "user_management/profile.html", {"profile": profile})

@login_required
def profile_update(request):
    """
    View to update the logged-in user's profile.
    """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user_management:profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "user_management/profile_form.html", {"form": form})

@login_required
def home_view(request):
    return render(request, "home.html")

def register(request):
    """
    View for user registration.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optional: Automatically log in the user after registering
            login(request, user)
            return redirect("user_management:profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/registration.html", {"form": form})