# Generated by Django 4.0.4 on 2022-05-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdi', '0002_answers_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question_id',
            field=models.IntegerField(default=0),
        ),
    ]