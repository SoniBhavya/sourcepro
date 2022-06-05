from django.db import models

class Mail_Table(models.Model):
    objects = models.Manager()
    email = models.CharField(max_length=30,default="")
    u_name = models.CharField(max_length=30)




