from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


def index(request):
    return render(request, "core/core_base.html")


class CaptureView(LoginRequiredMixin, TemplateView):
    template_name = "core/capture.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Capture.objects.filter(user=self.request.user).exists():
            context["capturehistory"] = Capture.objects.filter(
                user=self.request.user
            ).order_by("-date")
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            pk = request.POST.get("delete")
            capture = get_object_or_404(Capture, id=pk, user=request.user)
            capture.delete()

        if "capturearea" in request.POST:
            text = request.POST.get("capturearea", "")
            capture = Capture(user=request.user, text=text)
            capture.save()

        return redirect("core:capture")


class OrganizeView(LoginRequiredMixin, TemplateView):
    template_name = "core/organize.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not GoalTree.objects.filter(user=self.request.user).exists():
            tree = GoalTree(user=self.request.user)
            tree.save()
            for a in AreaOfDevelopment:
                domain = Domain(name=a, goal_tree=tree)
                domain.save()
        context["tree"] = GoalTree.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if "tree" in request.POST:
            pass


def organize(request):
    return render(request, "core/organize.html")


def plan(request):
    return render(request, "core/plan.html")


def focus(request):
    return render(request, "core/focus.html")


@login_required
def profile(request):
    user = request.user
    c = {
        "username": user.username,
        "email": user.email,
    }
    return render(request, "core/profile.html", c)


def settings(request):
    return render(request, "core/settings.html")
