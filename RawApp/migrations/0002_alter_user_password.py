# Generated by Django 5.0 on 2023-12-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RawApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
