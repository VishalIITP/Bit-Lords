# Generated by Django 3.1.5 on 2021-02-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210213_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='task',
            field=models.TextField(blank=True, null=True),
        ),
    ]
