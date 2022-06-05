from django.db import models
from django.db.models.fields import PositiveSmallIntegerField

# Create your models here.
class all_courses(models.Model):
    # objects = models.Manager()
    Course_id = models.CharField(max_length= 5, primary_key=True)
    course_name = models.CharField(max_length= 20)
    total_duration = models.CharField(max_length= 20)
    thumbnail = models.CharField(max_length= 20)
    chapters_vls = models.TextField(max_length= 100)
    course_description = models.CharField(max_length= 20)
    FAQs = models.CharField(max_length = 30)
    type = models.CharField(max_length=5, default= "none")


class usr_course(models.Model):
    objects = models.Manager()
    Course_id = models.CharField(max_length= 20, primary_key= True)
    status = models.CharField(max_length= 20)
    deactivation_days_left = models.CharField(max_length= 20)
    course_release_date = models.CharField(max_length= 20)
    percentage_completed = PositiveSmallIntegerField()
    minutes_Completed = PositiveSmallIntegerField()
    minutes_left = models.PositiveSmallIntegerField()


class quizes(models.Model):
    course_id = models.CharField(max_length = 5, primary_key = True)
    que_options = models.TextField(max_length = 500)