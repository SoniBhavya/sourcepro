# Generated by Django 4.0.4 on 2022-06-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcepro', '0006_rename_usr_courses_usr_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usr_course',
            name='minutes_Completed',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='usr_course',
            name='minutes_left',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='usr_course',
            name='percentage_completed',
            field=models.CharField(default=0, max_length=3),
        ),
    ]