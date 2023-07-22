from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError


def login(request):
    errmsg = request.GET.get("errmsg")
    return render(request, "login/base_login.html", {"errmsg": errmsg})


def authenticate_user(request):
    if request.method != "POST":
        return redirect(reverse("login:login"))

    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)

    if user is None:
        errmsg = "Email or password was not found."
        return redirect(reverse("login:login") + f"?errmsg={errmsg}")

    login(request, user)
    return redirect(reverse("core:core"))


def signup(request):
    errmsg = request.GET.get("errmsg")
    return render(request, "login/signup.html", {"errmsg": errmsg})


def register_user(request):
    if request.method != "POST":
        return redirect("login:signup")

    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]

    emailexists = User.objects.filter(email=email).exists()
    userexists = User.objects.filter(username=username).exists()
    passwordvalid, passerror = _validatepassword(password)

    err = None
    if emailexists or userexists:
        field = "email" if emailexists else "username"
        err = f"Please choose a different {field}. This {field} is already registered."
    elif not passwordvalid:
        err = f"Please choose a stronger password.\n{''.join([e for e in passerror])}"

    if err:
        return redirect(reverse("login:signup") + f"?errmsg={err}")

    User.objects.create_user(username=username, email=email, password=password)
    return redirect(reverse("core:core"))


def _validatepassword(password: str) -> tuple[bool, list[str]]:
    """
    Returns True on validate success with list of error messages.
    Returns empty list on success
    """
    try:
        validate_password(password)
    except ValidationError as e:
        error_messages = list(e.messages)  # unused
        return (False, error_messages)
    else:
        return (True, [])
