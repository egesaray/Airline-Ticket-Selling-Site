# Generated by Django 3.1.4 on 2021-01-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_feedback_adminresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='arrival_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_hour',
            field=models.TimeField(null=True),
        ),
    ]