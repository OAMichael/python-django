# Generated by Django 5.1.7 on 2025-04-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_graphics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
