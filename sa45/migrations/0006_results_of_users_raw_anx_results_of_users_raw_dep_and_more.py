# Generated by Django 4.0.4 on 2022-05-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa45', '0005_alter_results_of_users_global_severity_index_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='results_of_users',
            name='raw_anx',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_dep',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_hos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_int',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_oc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_par',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_pho',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_psy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='results_of_users',
            name='raw_som',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='results_of_users',
            name='global_severity_index',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='results_of_users',
            name='positive_symptom_total',
            field=models.IntegerField(),
        ),
    ]
