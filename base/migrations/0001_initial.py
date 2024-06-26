# Generated by Django 4.2 on 2024-06-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('quiz_length', models.IntegerField()),
                ('time', models.IntegerField(help_text='minutes')),
                ('pass_mark', models.IntegerField(help_text='minimum required score')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
    ]
