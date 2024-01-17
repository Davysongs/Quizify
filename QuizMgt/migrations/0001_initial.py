# Generated by Django 5.0.1 on 2024-01-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('optionA', models.CharField(max_length=200)),
                ('optionB', models.CharField(max_length=200)),
                ('optionC', models.CharField(max_length=200)),
                ('optionD', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('General-Studies', 'General Studies'), ('history', 'history'), ('Current-Affairs', 'Current Affairs'), ('Mathematics', 'Mathematics')], max_length=20)),
            ],
        ),
    ]
