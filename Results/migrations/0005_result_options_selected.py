# Generated by Django 5.0.1 on 2024-01-30 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Results', '0004_alter_result_result_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='options_selected',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]