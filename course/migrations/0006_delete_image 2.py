# Generated by Django 4.0.4 on 2022-05-10 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_category_id_course_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
