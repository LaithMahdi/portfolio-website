import os
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from configuration import models
from django.urls import reverse
from django.contrib import messages 
# Create your views here.

# acceuil
def acceuil(request):
    exp=models.Experience.objects.all().values
    profil=models.Profil.objects.all()
    skill = models.skills.objects.all().values
    certif=models.Certifications.objects.all()
    service =models.Services.objects.all()
    template = loader.get_template('home.html')
    context = {
        'exp':exp,
        'profil':profil,
        'skill':skill,
        'certif': certif,
        'service': service,
    }
    return HttpResponse(template.render(context, request))


# description 
def description(request):
    profil = models.Profil.objects.all()
    template = loader.get_template('description.html')
    context = {
    'profil': profil,
    }
    return HttpResponse(template.render(context, request))

def update_informations(request, id):
    profil=models.Profil.objects.get(id=id)
    template = loader.get_template('update_infGeneral.html')
    context = {
    'profil': profil,
    }
    return HttpResponse(template.render(context, request))
def update_infGeneral_action(request,id):
    profil=models.Profil.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(profil.photo) > 0:
                os.remove(profil.photo.path)
            profil.photo = request.FILES['photo']
        profil.nom=request.POST['nom']
        profil.prenom=request.POST['prenom'] 
        profil.poste=request.POST['poste']
        profil.lieu=request.POST['lieu']
        profil.description=request.POST['description']
        profil.mail=request.POST['mail']
        profil.tel=request.POST['tel']
        profil.linkdin=request.POST['linkdin']
        profil.behance=request.POST['behance']
        profil.git=request.POST['git']
        profil.fb=request.POST['fb']
        
        
        profil.save()
    return HttpResponseRedirect(reverse('acceuil'))
def ajouterDescription(request):
    if request.method == "POST":
        info=models.Profil()
        info.nom=request.POST.get('nom')
        info.prenom=request.POST.get('prenom')
        info.poste=request.POST.get('poste')
        info.lieu=request.POST.get('lieu')
        info.description=request.POST.get('description')
        info.mail=request.POST.get('mail')
        info.tel=request.POST.get('tel')
        info.linkdin=request.POST.get('linkdin')
        info.behance=request.POST.get('behance')
        info.git=request.POST.get('git')
        info.fb=request.POST.get('fb')
        if len(request.FILES)!=0:
            info.photo=request.FILES['photo']
        info.save()
        messages.success(request,'Description ajoute')
        return redirect('acceuil')
    return render(request,'ajouteDescription.html')
def delete_infGeneral(resuest,id):
    profil=models.Profil.objects.get(id=id)
    profil.delete()
    return redirect('acceuil')

# Experience 
def experience(request):
    exp = models.Experience.objects.all()
    template = loader.get_template('expereince.html')
    context = {
    'exp': exp,
    }
    return HttpResponse(template.render(context, request))

def ajouterExpereince(request):
    if request.method == "POST":
        exp=models.Experience()
        exp.nom=request.POST.get('nom')
        exp.post=request.POST.get('post')
        exp.date=request.POST.get('date')
        exp.tache=request.POST.get('tache')
        exp.save()
        messages.success(request,'Expérience ajoute avec success ')
        return redirect('acceuil')
    return render(request,'ajouterExpereince.html')
def update_Experience(request, id):
    exp=models.Experience.objects.get(id=id)
    template = loader.get_template('update_Experience.html')
    context = {
    'exp': exp,
    }
    return HttpResponse(template.render(context, request))
    

def update_Experience_action(request,id):
    exp=models.Experience.objects.get(id=id)
    if request.method == "POST":
        exp.nom=request.POST['nom']
        exp.post=request.POST['post']
        exp.date=request.POST['date']
        exp.tache=request.POST['tache']
        exp.save()
    return HttpResponseRedirect(reverse('acceuil'))

    
def delete_Experience(resuest,id):
    exp=models.Experience.objects.get(id=id)
    exp.delete()
    return redirect('experience')

def competence(request):
    skill = models.skills.objects.all()
    template = loader.get_template('skills.html')
    context = {
    'skill': skill,
    }
    return HttpResponse(template.render(context, request))

def ajouterCompetence(request):
    if request.method == "POST":
        skill=models.skills()
        skill.nom=request.POST.get('nom')
        skill.niveau=request.POST.get('niveau')
        skill.type=request.POST.get('type')
        skill.save()
        messages.success(request,'Compétence ajoute avec success ')
        return redirect('acceuil')
    return render(request,'ajouterCompetence.html')
def delete_competence(resuest,id):
    skill=models.skills.objects.get(id=id)
    skill.delete()
    return redirect('acceuil')

def update_competence(request,id): 
    skill=models.skills.objects.get(id=id)
    template = loader.get_template('update_competence.html')
    context = {
    'skill': skill,
    }
    return HttpResponse(template.render(context, request))
def update_competence_action(request,id):
    skill=models.skills.objects.get(id=id)
    if request.method == "POST":
        skill.nom=request.POST['nom']
        skill.type=request.POST['type']
        skill.niveau=request.POST['niveau']
        skill.save()
    return HttpResponseRedirect(reverse('acceuil'))

def certifications(request):
    certif = models.Certifications.objects.all()
    template = loader.get_template('certifications.html')
    context = {
    'certif': certif,
    }

    return HttpResponse(template.render(context, request))

def ajouterCertification(request):
    if request.method == "POST":
        certif=models.Certifications()
        certif.nom=request.POST.get('nom')
        certif.lien=request.POST.get('lien')
        certif.date=request.POST.get('date')
        if len(request.FILES)!=0:
            certif.photo=request.FILES['photo']
        certif.save()
        messages.success(request,'Description ajoute')
        return redirect('acceuil')
    return render(request,'ajouterCertification.html')

def update_Certification(request, id):
    certif = models.Certifications.objects.get(id=id)
    template = loader.get_template('update_Certification.html')
    context = {
    'certif': certif,
    }
    return HttpResponse(template.render(context, request))

def update_Certification_action(request, id):
    certif = models.Certifications.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(certif.photo) > 0:
                os.remove(certif.photo.path)
            certif.photo = request.FILES['photo']
        certif.nom=request.POST['nom']
        certif.date=request.POST['date']
        certif.lien=request.POST['lien']
        certif.save()
        return HttpResponseRedirect(reverse('acceuil'))

def delete_Certification(request,id):
    certif = models.Certifications.objects.get(id=id)
    certif.delete()
    return redirect('acceuil')

def porjet(request):
    projet = models.Projets.objects.all()
    template = loader.get_template('project.html')
    context = {
    'projet': projet,
    }

    return HttpResponse(template.render(context, request))

def ajouterProjet(request):
    if request.method == "POST":
        projet=models.Projets()
        projet.nom=request.POST.get('nom')
        projet.lien=request.POST.get('lien')
        projet.date=request.POST.get('date')
        projet.tache=request.POST.get('tache')
        projet.save()
        messages.success(request,'Projet ajoute')
        return redirect('acceuil')
    return render(request,'ajouteProjet.html')

def delete_porjet(request,id):
    projet = models.Projets.objects.get(id=id)
    projet.delete()
    return redirect('acceuil')

def update_porjet(request, id):
    projet = models.Projets.objects.get(id=id)
    template = loader.get_template('update_projet.html')
    context = {
    'projet': projet,
    }
    return HttpResponse(template.render(context, request))

def update_porjet_action(request, id):
    projet = models.Projets.objects.get(id=id)
    if request.method == "POST":
        projet.nom=request.POST['nom']
        projet.date=request.POST['date']
        projet.lien=request.POST['lien']
        projet.tache=request.POST['tache']
        projet.save()
        return HttpResponseRedirect(reverse('acceuil'))

def services(request):
    service = models.Services.objects.all()
    template = loader.get_template('services.html')
    context = {
    'service': service,
    }
    return HttpResponse(template.render(context, request))

def ajouterService(request):
    if request.method == "POST":
        service=models.Services()
        service.nom=request.POST.get('nom')
        service.icon=request.POST.get('icon')
        service.description=request.POST.get('description')
        service.save()
        messages.success(request,'Service ajoute')
        return redirect('acceuil')
    return render(request,'ajouteServices.html')

def delete_services(request,id):
    service = models.Services.objects.get(id=id)
    service.delete()
    return redirect('services')

def update_services(request,id):
    service = models.Services.objects.get(id=id)
    template = loader.get_template('update_Service.html')
    context = {
    'service': service,
    }
    return HttpResponse(template.render(context, request))
def update_services_action(request,id):
    service = models.Services.objects.get(id=id)
    if request.method == "POST":
        service.nom=request.POST['nom']
        service.description=request.POST['description']
        service.icon=request.POST['icon']
        service.save()
        return HttpResponseRedirect(reverse('services'))

def langue(request):
    langue = models.Langue.objects.all()
    template = loader.get_template('langue.html')
    context = {
    'langue': langue,
    }
    return HttpResponse(template.render(context, request))
def ajouterLangue(request):
    if request.method == "POST":
        langue=models.Langue()
        langue.nom=request.POST.get('nom')
        langue.niveau=request.POST.get('niveau')
        langue.save()
        messages.success(request,'Langue ajoute')
        return redirect('langue')
    return render(request,'ajouteLangue.html')

def update_langue(request,id):
    langue = models.Langue.objects.get(id=id)
    template = loader.get_template('update_langue.html')
    context = {
    'langue': langue,
    }
    return HttpResponse(template.render(context, request))
def update_langue_action(request,id):
    langue = models.Langue.objects.get(id=id)
    if request.method == "POST":
        langue.nom=request.POST['nom']
        langue.niveau=request.POST['niveau']
        langue.save()
        return HttpResponseRedirect(reverse('langue'))

def delete_langue(request,id):
    langue = models.Langue.objects.get(id=id)
    langue.delete()
    return redirect('langue')