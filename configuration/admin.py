from django.contrib import admin
from configuration.models import Profil,Experience,skills,Projets,Certifications,Langue,Services
# Register your models here.

# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','description','mail','lieu','photo','poste','linkdin','behance','git','fb','tel')
    list_filter = ('nom', 'lieu', 'poste')
    search_fields = ('nom', 'prenom', 'poste')

class ExperienceAdmin(admin.ModelAdmin):
    list_display=('nom','post','tache','date')
    list_filter =('date','nom','post')
    search_fields = ('nom', 'post')

class SkillsAdmin(admin.ModelAdmin):
    list_display=('nom','type','niveau')
    list_filter =('niveau','type')
    search_fields = ('nom', 'type')

class ProjetsAdmin(admin.ModelAdmin):
    list_display=('nom','tache','date','lien')
    list_filter =('date','nom')
    search_fields = ('nom', 'post','date')

class CertificationsAdmin(admin.ModelAdmin):
    list_display=('nom','photo','lien','date')
    list_filter =('date','nom')
    search_fields = ('nom','date')

class LangueAdmin(admin.ModelAdmin):
    list_display=('nom','niveau')
    list_filter =('nom','niveau')
    search_fields = ('nom','niveau')

class ServicesAdmin(admin.ModelAdmin):
    list_display=('nom','icon','description')

admin.site.register(Profil,ProfilAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(skills,SkillsAdmin)
admin.site.register(Projets,ProjetsAdmin)
admin.site.register(Certifications,CertificationsAdmin)
admin.site.register(Langue,LangueAdmin)
admin.site.register(Services,ServicesAdmin)