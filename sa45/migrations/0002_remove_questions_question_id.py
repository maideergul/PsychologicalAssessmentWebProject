# Generated by Django 4.0.4 on 2022-05-18 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sa45', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='question_id',
        ),
    ]
