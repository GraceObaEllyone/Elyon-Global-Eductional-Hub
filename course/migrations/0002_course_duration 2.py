# Generated by Django 4.0.4 on 2022-05-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.IntegerField(default=0, max_length=6),
        ),
    ]