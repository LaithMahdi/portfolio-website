import datetime
import os
from django.db import models

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('static/uploads/', filename)

class Profil(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    description=models.TextField()
    mail=models.CharField(max_length=50)
    lieu=models.CharField(max_length=50)
    photo=models.ImageField(upload_to=filepath,null=True,blank=True)
    poste=models.CharField(max_length=150)
    linkdin=models.CharField(max_length=250,null=True)
    behance=models.CharField(max_length=250,null=True)
    git=models.CharField(max_length=250,null=True)
    fb=models.CharField(max_length=250,null=True)
    tel=models.CharField(max_length=250,null=True)

class Experience (models.Model):
    nom=models.CharField(max_length=200)
    post=models.CharField(max_length=200, null=True)
    tache=models.TextField()
    date=models.DateField()

class skills (models.Model):
    type=models.IntegerField(default=1)
    nom=models.CharField(max_length=100)
    niveau=models.IntegerField(null=True,default=0)

class Projets(models.Model):
    nom=models.CharField(max_length=200)
    tache=models.TextField()
    date=models.DateField()
    lien=models.CharField(max_length=300,null=True)

class Certifications(models.Model):
    nom=models.CharField(max_length=300)
    photo=models.ImageField(upload_to=filepath,blank=True)
    lien=models.CharField(max_length=300,null=True)
    date=models.DateField()

class Langue(models.Model):
    nom=models.CharField(max_length=100)
    niveau=models.IntegerField(null=True)

class Services(models.Model):
    nom=models.CharField(max_length=100)
    icon=models.CharField(max_length=300)
    description=models.TextField()