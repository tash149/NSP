# Generated by Django 2.0.6 on 2018-07-01 06:34

import datetime
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
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', 'Open'), ('0', 'Closed')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='IssueComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=50)),
                ('mentor_name', models.CharField(default='', max_length=50)),
                ('branch', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(max_length=2500)),
                ('paid', models.BooleanField(default=False)),
                ('start_date', models.DateField(default=datetime.datetime.now)),
                ('initiated_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPeopleInterested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='accounts.ProjectDetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(blank=True, default='', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('0', 'Open'), ('1', 'Accepted'), ('2', 'Not Accepted')], max_length=1)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_solution', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolutionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Solution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField(blank=True, default=0, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('year', models.IntegerField(blank=True, default=1, null=True)),
                ('branch', models.CharField(blank=True, default='Not Updated', max_length=20, null=True)),
                ('stream', models.CharField(blank=True, default='Not Updated', max_length=20, null=True)),
                ('gender', models.CharField(blank=True, default='Not Updated', max_length=20, null=True)),
                ('position', models.CharField(blank=True, default='Not Updated', max_length=20, null=True)),
                ('bio', models.CharField(blank=True, default='', max_length=500)),
                ('follows', models.ManyToManyField(blank=True, related_name='followers', to='accounts.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounts_userprofile',
            },
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProjectDetail'),
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
