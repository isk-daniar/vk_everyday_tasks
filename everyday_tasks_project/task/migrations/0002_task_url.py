# Generated by Django 4.1.7 on 2023-12-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='url',
            field=models.SlugField(default=0, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]
