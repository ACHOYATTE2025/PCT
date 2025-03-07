from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from xml.dom.minidom import Document


urlpatterns = [
    path('', views.index,name='base1'),
    path('acteur_list/',views.acteur_list , name='acteur_list'),
    path('acteur_details/<int:pk>/', views.acteur_details, name='acteur_details'),
    path('acteurs/<int:pk>/',views.acteur_edit, name='acteur_edit'),
    path('acteurs/Ajouter/',views.acteur_edit, name='acteur_edit'),
    path('services_acteur/',views.services_acteur , name='services_acteur'),
    path('acteur_list/<int:pk>/',views.acteur_delete , name='acteur_delete'),
    path('pharmacie_list/',views.pharmacie_list , name='pharmacie_list'),
    path('pharmacie_details/<int:pk>/', views.pharmacie_details, name='pharmacie_details'),
    path('pharmacie/<int:pk>/',views.pharmacie_edit , name='pharmacie_edit'),
    path('pharmacie/Ajouter/',views.pharmacie_edit , name='pharmacie_edit'),
    path('services_pharmacie/',views.services_pharmacie , name='services_pharmacie'),
    path('pharmacie_list/<int:pk>/',views.pharmacie_delete , name='pharmacie_delete'),
    path('galerie', views.galerie , name='galerie'),   
    path('services_naissance/',views.services_naissance, name='services_naissance'),
    path('naissance_list/',views.naissance_list,name='naissance_list'),
    path('naissance_details/<int:pk>/', views.naissance_details, name='naissance_details'),
    path('naissance_list/<int:pk>/',views.naissance_delete , name='naissance_delete'),
    path('naissance/<int:pk>/',views.naissance_edit , name='naissance_edit'),
    path('naissance/Ajouter/',views.naissance_edit , name='naissance_edit'),
    path('services_deces/',views.services_deces, name='services_deces'),
    path('deces_list/',views.deces_list, name='deces_list'),
    path('deces_edit/<int:pk>/',views.deces_edit, name='deces_edit'),
    path('deces_edit/Ajouter/',views.deces_edit, name='deces_edit'),
    path('services_deces/<int:pk>/',views.deces_delete, name='deces_delete'),
    path('services_recherche_emploi/',views.services_recherce_emploi, name='services_recherche_emploi'),
    path('recherche_emploi_list', views.recherche_emploi_list,name='recherche_emploi_list'),
    path('recherche_emploi/<int:pk>/',views.recherche_emploi_edit , name='recherche_emploi_edit'),
    path('recherche_emploi/Ajouter/',views.recherche_emploi_edit , name='recherche_emploi_edit'),
    path('services_recherche_emploi/<int:pk>/',views.recherche_delete, name='recherche_delete'),
    path('services_mouvement/',views.services_mouvement, name='services_mouvement'),
    path('amenageant_list/',views.mouvement_a_list , name='amenageant_list'),
    path('amenageant_edit/<int:pk>/',views.amenageant_edit, name='amenageant_edit'),
    path('amenageant_edit/Ajouter/',views.amenageant_edit, name='amenageant_edit'),
    path('services_mouvement/<int:pk>/',views.amenageant_delete, name='amenageant_delete')
    
   ] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)