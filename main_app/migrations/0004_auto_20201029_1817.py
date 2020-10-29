# Generated by Django 3.1.2 on 2020-10-29 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201029_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reguser',
            name='id',
        ),
        migrations.AlterField(
            model_name='reguser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
