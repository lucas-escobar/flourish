from django.urls import path

from . import views

app_name = "login"

urlpatterns = [
    path("", views.login, name="login"),
    path("auth/", views.authenticate_user, name="auth"),
    path("signup/", views.signup, name="signup"),
    path("register/", views.register_user, name="register"),
]
