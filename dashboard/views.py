from django.shortcuts import render,  get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from gestion.models import Acteur, Naissance,Deces,Pharmacie,Recherche_emploi,Venant



# Create your views here.


def dashboard( request):
  aff= False
  user = User.objects.all()
  if request.user.username == 'admin':
    dash = 'active'
  else:
    dash = 'disabled'
  nombre_pharmacie =Pharmacie.objects.count()
  nombre_acteur = Acteur.objects.count()
  nombre_naissance = Naissance.objects.count()
  nombre_deces = Deces.objects.count()
  nombre_recherche_emploi = Recherche_emploi.objects.count()
  nombre_amenageant = Venant.objects.count()
  
  pharmacie = Pharmacie.objects.all()
  acteur = Acteur.objects.all()
  naissance = Naissance.objects.all()
  deces = Deces.objects.all()
  recherche_emploi = Recherche_emploi.objects.all()
  amenageant = Venant.objects.all()
  
  new_naissance_list = []
  new_emploi_list = []
  new_deces_list = []
  new_acteur_list = []
  new_amenageant_list = []
  
  if naissance:
    for item in naissance:
      if (item.valide == 0 and item.statut =='non') :
        aff = True
      else:
        aff = False
      new_naissance_list.append({'naissance':item,'aff': aff})
       

  
  if recherche_emploi:
    for item in recherche_emploi:
      if (item.valide == 0 and item.statut =='non') :
        aff = True
      else:
        aff:False
      new_emploi_list.append({'emploi':item,'aff': aff})
        
  if deces:
    for item in deces:
      if (item.valide == 0) and (item.statut =='non') :
        aff = True
      else:
        aff = False
      new_deces_list.append({'deces':item,'aff': aff})
  
  if acteur:
    for item in acteur:
      if (item.valide == 0 or item.statut =='non') :
        aff = True
        new_acteur_list.append({'acteur':item,'aff': aff})      
        
        
  
  if amenageant :
    for item in amenageant:
      if (item.valide == 0 or item.statut =='non') :
        aff = True
        new_amenageant_list.append({'amenageant':item,'aff': aff})
  
  
  
  context ={'nombre_acteur': nombre_acteur,
            'nombre_naissance':nombre_naissance,
            'nombre_deces':nombre_deces,
            'nombre_pharmacie' : nombre_pharmacie,
            'nombre_recherche_emploi':nombre_recherche_emploi,
            'nombre_amenageant':nombre_amenageant, 
            'dash':dash,
            'new_naissance':new_naissance_list,
            'emploi':new_emploi_list,
            'deces':new_deces_list,
            'acteur':new_acteur_list,
            'amenageant':new_amenageant_list
            
    
    
  }
  return render(request,'dashboard/dashboard.html',context)