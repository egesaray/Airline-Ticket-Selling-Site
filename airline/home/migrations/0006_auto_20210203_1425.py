# Generated by Django 3.1.4 on 2021-02-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210203_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='gate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='terminal',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]