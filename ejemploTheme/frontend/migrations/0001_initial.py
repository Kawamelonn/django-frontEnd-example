# Generated by Django 4.1.7 on 2023-04-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]
