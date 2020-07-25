from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    userName = models.CharField('name', unique=True, max_length=50)
    email = models.CharField('email', unique=True, max_length=50)
    password = models.CharField('password', max_length=50)
    buildTime = models.DateTimeField('buildTime')
    headPic = models.CharField('headPic', default="../../../assets/default-head.jpg", max_length=255)
    readme = models.CharField('readme', blank=True, max_length=255)
    mood = models.CharField('mood', blank=True, max_length=255)
    job = models.IntegerField('job', default=0)
    place = models.CharField('place', blank=True, max_length=50)
    class Meta:
        db_table = 'user'

class Verification(models.Model):
    email = models.CharField('email', max_length=30)
    code = models.IntegerField('code')
    askTime = models.DateTimeField('askTime', auto_now=True)
    failureTime = models.DateTimeField('failureTime')
    class Meta:
        db_table = 'codeTable'
