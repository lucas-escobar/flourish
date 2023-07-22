from django.urls import path

from . import views
from .views import *

app_name = "core"

urlpatterns = [
    path("", views.index, name="core"),
    path("capture/", CaptureView.as_view(), name="capture"),
    path("organize/", OrganizeView.as_view(), name="organize"),
    path("plan/", views.plan, name="plan"),
    path("focus/", views.focus, name="focus"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
]
