from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("announcement_list")
    else: # it's a "GET" request
        form = UserRegistrationForm()
    return render(request, "core/register.html", {"form": form})

