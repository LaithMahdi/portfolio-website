from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from configuration import models
# Create your views here.
def index(request):
    exp=models.Experience.objects.all().values
    profil=models.Profil.objects.all()
    skill = models.skills.objects.all().values
    services = models.Services.objects.all().values
    projet = models.Projets.objects.all().values
    certicat = models.Certifications.objects.all()
    template = loader.get_template('index.html')
    context = {
        'exp':exp,
        'profil':profil,
        'skill':skill,
        'services':services,
        'projet':projet,
        'certicat':certicat,
    }
    return HttpResponse(template.render(context, request))