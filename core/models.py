from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

import typing


class AreaOfDevelopment(models.TextChoices):
    PROFESSIONAL = "professional"
    SOCIAL = "social"
    SPIRITUAL = "spiritual"
    PHYSICAL = "physical"
    CREATIVE = "creative"
    ENVIRONMENTAL = "environmental"


class Priority(models.TextChoices):
    ESSENTIAL = "essential"
    PROACTIVE = "proactive"
    OPTIONAL = "optional"


class GoalTree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=20, choices=AreaOfDevelopment.choices)
    goal_tree = models.ForeignKey(GoalTree, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Goal(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=Priority.choices)
    is_achieved = models.BooleanField()


class Project(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deadline = models.DateField()


class Task(models.Model):
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=Priority.choices)
    needcomputer = models.BooleanField(
        verbose_name="does this task require a computer?"
    )
    repeats = models.CharField(max_length=10)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    parent = GenericForeignKey("content_type", "object_id")


class Capture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"Capture #{self.id} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
