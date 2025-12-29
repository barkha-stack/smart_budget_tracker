from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def signup(request):
    """
    Handles user registration
    """

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after signup
            return redirect("/finance/")  # dashboard
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})
