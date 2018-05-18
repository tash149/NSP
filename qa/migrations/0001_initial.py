# Generated by Django 2.0 on 2018-05-18 18:41

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models
import markdownx.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', markdownx.models.MarkdownxField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('answer', models.BooleanField(default=False)),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-answer', '-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('comment_text', markdownx.models.MarkdownxField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Answer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', markdownx.models.MarkdownxField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('reward', models.IntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
                ('total_points', models.IntegerField(default=0)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('comment_text', models.CharField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(default=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserQAProfile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('points', models.IntegerField(default=0)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='questionvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answervote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='questionvote',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='answervote',
            unique_together={('user', 'answer')},
        ),
    ]
