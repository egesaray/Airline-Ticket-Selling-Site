# Generated by Django 3.1.4 on 2021-01-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210109_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='adminresponse',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
