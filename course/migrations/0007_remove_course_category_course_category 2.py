# Generated by Django 4.0.4 on 2022-05-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='course.category'),
        ),
    ]
