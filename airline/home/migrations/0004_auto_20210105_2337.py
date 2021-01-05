# Generated by Django 3.1.4 on 2021-01-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210105_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_id',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='type',
            field=models.CharField(choices=[('request', 'request'), ('suggestion', 'suggestion'), ('complaint', 'complaint')], max_length=255, null=True),
        ),
    ]