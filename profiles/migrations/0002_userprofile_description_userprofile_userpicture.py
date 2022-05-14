# Generated by Django 4.0.4 on 2022-05-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userPicture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
