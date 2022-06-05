from django.db import models

class login_details(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=30,default="", primary_key=True)
    password = models.CharField(max_length=30)

class user_details(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class all_course(models.Model):
    objects = models.Manager()
    id = models.CharField(max_length= 20, primary_key=True)
    name = models.CharField(max_length= 20)
    total_duration = models.CharField(max_length= 20)
    thumbnail = models.CharField(max_length= 20)
    chapters_vls = models.CharField(max_length= 100)
    course_description = models.CharField(max_length= 20)
    FAQs = models.CharField(max_length = 20)

class user_courses(models.Model):
    objects = models.Manager()
    Course_id = models.CharField(max_length= 20, primary_key= True)
    status = models.CharField(max_length= 20)
    deactivation_days_left = models.CharField(max_length= 20)
    course_release_date = models.CharField(max_length= 20)
