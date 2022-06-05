from django.db import models
from django.db.models.fields import PositiveSmallIntegerField


# Create your models here.
class all_courses(models.Model):
    # objects = models.Manager()
    Course_id = models.CharField(max_length=5, primary_key=True)
    course_name = models.CharField(max_length=20)
    total_duration = models.PositiveSmallIntegerField(max_length=20)  # integer
    thumbnail = models.CharField(max_length=20)
    # chapters_vls = models.TextField(max_length=100)
    course_description = models.TextField(max_length=20)  # textfield
    FAQs = models.CharField(max_length=30)  # textfield
    type = models.CharField(max_length=5, default="none")
    author = models.CharField(max_length=20, default="name of author")


class usr_course(models.Model):
    objects = models.Manager()
    Course_id = models.CharField(max_length=20, primary_key=True)
    status = models.CharField(max_length=20)
    deactivation_days_left = models.PositiveSmallIntegerField()  # interger
    course_release_date = models.CharField(max_length=20)
    percentage_completed = models.PositiveSmallIntegerField()
    minutes_Completed = models.PositiveSmallIntegerField()
    minutes_left = models.PositiveSmallIntegerField()


class quizes(models.Model):
    course_id = models.CharField(max_length=5, primary_key=True)
    que_options = models.TextField(max_length=500)


