# Generated by Django 3.1.4 on 2021-01-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_feedback_is_ok'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='my_points',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
