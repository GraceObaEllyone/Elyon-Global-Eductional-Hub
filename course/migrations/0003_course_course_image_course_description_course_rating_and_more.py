# Generated by Django 4.0.4 on 2022-04-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_course_id_coursereview_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254)),
                ('image', models.ImageField(upload_to='')),
                ('URL', models.URLField(blank=True, max_length=1024)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course')),
            ],
        ),
    ]
