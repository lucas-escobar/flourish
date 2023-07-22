# Generated by Django 4.2.3 on 2023-07-18 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('professional', 'Professional'), ('social', 'Social'), ('spiritual', 'Spiritual'), ('physical', 'Physical'), ('creative', 'Creative'), ('environmental', 'Environmental')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('prio', models.CharField(choices=[('essential', 'Essential'), ('proactive', 'Proactive'), ('optional', 'Optional')], max_length=20)),
                ('needcomputer', models.BooleanField()),
                ('repeats', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('milestones', models.ManyToManyField(related_name='projects', to='core.task')),
            ],
        ),
        migrations.CreateModel(
            name='GoalTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domains', models.ManyToManyField(related_name='goal_trees', to='core.domain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('prio', models.CharField(choices=[('essential', 'Essential'), ('proactive', 'Proactive'), ('optional', 'Optional')], max_length=20)),
                ('is_achieved', models.BooleanField()),
                ('projects', models.ManyToManyField(related_name='goals', to='core.project')),
                ('tasks', models.ManyToManyField(related_name='goals', to='core.task')),
            ],
        ),
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]