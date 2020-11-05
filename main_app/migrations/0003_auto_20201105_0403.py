# Generated by Django 3.1.2 on 2020-11-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_reguser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.CharField(default='photo.jpg', max_length=250),
        ),
        migrations.AlterField(
            model_name='dog',
            name='story',
            field=models.TextField(default='story', max_length=1000),
        ),
        migrations.AlterField(
            model_name='provider',
            name='adoptionProcess',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='description',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='image',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
