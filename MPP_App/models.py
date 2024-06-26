from django.db import models

# Create your models here.
class MPP(models.Model):
    mppId=models.CharField(max_length=20, primary_key=True)
    mpppassword=models.CharField(max_length=15)
    mppname=models.CharField(max_length=20)
    
    
class ADMIN(models.Model):
    adminID=models.CharField(max_length=20, primary_key=True)
    adminName=models.CharField(max_length=20)
    adminEmail=models.EmailField()
    adminPassword=models.CharField(max_length=15)

class ACTIVITYASSIGN(models.Model):
    activityassignname=models.CharField(max_length=20, primary_key=True)
    activityassigndate=models.DateField()
    activityassignwork=models.TextField()
    activityassignmpp=models.TextField()
    activityassigndate2=models.DateField()
    activityassignperkara=models.TextField()

class ACTIVITY(models.Model):
    activityname=models.CharField(max_length=20, primary_key=True)
    activitystartdate=models.DateField()
    activityenddate=models.DateField()
    activityperkara=models.TextField()
    activityimage1 = models.ImageField(upload_to='activity_images/', blank=True, null=True)
    activityimage2 = models.ImageField(upload_to='activity_images/', blank=True, null=True)
    activityimage3 = models.ImageField(upload_to='activity_images/', blank=True, null=True)











    

