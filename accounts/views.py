# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProfileForm

@login_required
def account_settings(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated.")
            return redirect("account_settings")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "accounts/settings.html", {"form": form})
