from django.db import models
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext as _
from django.conf import settings

class ClientsData(models.Model):
    name = models.ForeignKey("Clients",null=True,blank=True)
    account = models.ForeignKey("Accounts",null=True,blank=True)
    total = models.IntegerField()
    completed = models.IntegerField()
    pending = models.IntegerField()
    added_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)
    def __unicode__(self):
       return _("%s") % self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Accounts(models.Model):
    acc_name = models.CharField(max_length=100)
    

    def __str__(self):              # __unicode__ on Python 2
        return self.acc_name


class Clients(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile=models.CharField(max_length=20,blank=True)
    email=models.EmailField(max_length=75,null=True)
    country = models.CharField(max_length=100, blank=True)
    joined_date = models.DateField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name



class Document(models.Model):
    docfile = models.FileField(upload_to='media')
