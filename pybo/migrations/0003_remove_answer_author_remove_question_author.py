# Generated by Django 5.0.07 on 2024-07-22 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_rename_quesiton_answer_question_answer_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
