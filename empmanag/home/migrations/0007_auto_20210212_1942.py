# Generated by Django 3.1.5 on 2021-02-12 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_auto_20210212_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
