from django.urls import path
from . import views
urlpatterns = [
    path('acceuil',views.acceuil,name='acceuil'),
    path('description',views.description,name='description'),
    path('acceuil/update_infGeneral/<int:id>',views.update_informations,name="update_informations"),
    path('acceuil/update_infGeneral/update_infGeneral_action/<int:id>',views.update_infGeneral_action,name="update_infGeneral_action"),
    path('ajouterDescription/',views.ajouterDescription,name="ajouterDescription"),
    path('acceuil/delete_infGeneral/<int:id>',views.delete_infGeneral,name='delete_infGeneral'),
    
    path('experience',views.experience,name='experience'),
    path('ajouterExpereince/',views.ajouterExpereince,name='ajouterExpereince'),
    path('experience/update_Experience/<int:id>',views.update_Experience,name='update_Experience'),
    path('experience/update_Experience/update_Experience_action/<int:id>',views.update_Experience_action,name='update_Experience_action'),
    path('experience/delete_Experience/<int:id>',views.delete_Experience,name='delete_Experience'),
    
    path('competence',views.competence,name='competence'),
    path('ajouterCompetence/',views.ajouterCompetence,name='ajouterCompetence'),
    path('competence/delete_competence/<int:id>',views.delete_competence,name='delete_competence'),
    path('competence/update_competence/<int:id>',views.update_competence,name='update_competence'),
    path('competence/update_competence/update_competence_action/<int:id>',views.update_competence_action,name='update_competence_action'),

    path('certifications',views.certifications,name="certifications"),
    path('ajouterCertification/',views.ajouterCertification,name='ajouterCertification'),
    path('certification/update_Certification/<int:id>',views.update_Certification,name="update_Certification"),
    path('certification/update_Certification/update_Certification_action/<int:id>',views.update_Certification_action,name='update_Certification_action'),
    path('certification/delete_Certification/<int:id>',views.delete_Certification,name='delete_Certification'),

    path('porjet',views.porjet,name='porjet'),
    path('ajouterProjet/',views.ajouterProjet,name='ajouterProjet'),
    path('porjet/delete_porjet/<int:id>',views.delete_porjet,name='delete_porjet'),
    path('porjet/update_porjet/<int:id>',views.update_porjet,name='update_porjet'),
    path('porjet/update_porjet/update_porjet_action/<int:id>',views.update_porjet_action,name='update_porjet_action'),

    path('services',views.services,name='services'),
    path('ajouterService/',views.ajouterService,name='ajouterService'),
    path('services/delete_services/<int:id>',views.delete_services,name='delete_services'),
    path('services/update_services/<int:id>',views.update_services,name='update_services'),
    path('services/update_services/update_services_action/<int:id>',views.update_services_action,name='update_services_action'),

    path('langue',views.langue,name='langue'),
    path('ajouterLangue/',views.ajouterLangue,name='ajouterLangue'),
    path('langue/update_langue/<int:id>',views.update_langue,name='update_langue'),
    path('langue/update_langue/update_langue_action/<int:id>',views.update_langue_action,name='update_langue_action'),
    path('langue/delete_langue/<int:id>',views.delete_langue,name='delete_langue'),
]