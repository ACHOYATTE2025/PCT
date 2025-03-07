from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .models import*
from django import forms
from .forms import ActeurForm, PharmacieForm, NaissanceForm, DecesForm, Recherche_emploiForm,guessActeurForm, GuessDecesForm,GuessNaissanceForm,GuessrechercheForm,VenantForm, GuessVenantForm,guessPharmacieForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.mail import send_mail, mail_admins
from django.http import HttpResponse

# Create your views here.

def index( request):
  nbre = 0
  aff=''
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
    dash = 'active'
  else:
    dash = 'disabled'
 
  
  pharmacie = Pharmacie.objects.all()
  acteur = Acteur.objects.all()
  naissance = Naissance.objects.all()
  deces = Deces.objects.all()
  recherche_emploi = Recherche_emploi.objects.all()
  amenageant = Venant.objects.all()
  
  
  
  nbre_naissance=0
  if naissance:
    for item in naissance:
      if (item.valide == 0 and item.statut =='non') :
        aff = True
        nbre_naissance += 1
      else:
        aff = False
    if nbre_naissance>0:
      code_naissance = 'deco'
      paint_naissance = 'red'
    else:
      code_naissance =''
      paint_naissance='purple'

  paint_emploi ="purple"
  code_emploi = ''
  nbre_emploi=0
  if recherche_emploi:
    nbre = 0
    for item in recherche_emploi:
      if (item.valide == 0 and item.statut =='non') :
        aff = True
        nbre_emploi += 1
      else:
        aff:False
      if nbre_emploi>0:
        code_emploi = 'deco'
        paint_emploi = 'red'
      else:
        code_emploi =''
        paint_emploi = 'purple'
      
  code_deces =''
  paint_deces ='purple'
  nbre_deces=0      
  if deces:
    nbre =0
    for item in deces:
      if (item.valide == 0) and (item.statut =='non') :
        aff = True
        nbre_deces +=1
      else:
        aff = False
      if nbre_deces > 0:
        code_deces = 'deco'
        paint_deces='red'
      else:
        code_deces =''
        paint_deces ='purple'
      
    
  nbre_acteur=0 
  if acteur:
    nbre =0
    for item in acteur:
      if (item.valide == 0 or item.statut =='non') :
        aff = True
        nbre_acteur +=1
         
        
        
  nbre_amena = 0
  code_amena =''
  paint_amena ='purple'
  if amenageant :
    nbre =0
    for item in amenageant:
      nbre_amena +=1
      if (item.valide == 0 or item.statut =='non') :
        aff = True
      if nbre_amena>0:
        code_amena= 'deco'
        paint_amena='red'
      else:
        code_amena =''
        paint_amena ='purple'
   
  show=False
  if nbre_naissance>0 or nbre_acteur>0 or nbre_deces>0 or nbre_emploi>0 or nbre_amena>0:
    show = True
  else:
    show =False
  
  
  
  context ={
            'dash':dash,
            'nbre_naissance':nbre_naissance,'code_naissance':code_naissance,'paint_naissance':paint_naissance,
            'nbre_emploi':nbre_emploi,'code_emploi':code_emploi,'paint_emploi':paint_emploi,
            'nbre_deces':nbre_deces,'code_deces':code_deces ,'paint_deces':paint_deces,
            'nbre_acteur':nbre_acteur,
            'nbre_amena':nbre_amena,'code_amena':code_amena ,'paint_amena':paint_amena ,
            'show':show,
             'firstname':firstname  
          }   
  
  return render(request, 'base1.html',context)

# fonctionnalités Acteur

def services_acteur(request):
  user = User.objects.all()
  firstname = request.user.username
  if request.user.username == 'admin':
    dash = 'active'
  else:
    dash = 'disabled'
  form = ActeurForm(instance=None)
  return render(request,'gestion/services_acteur.html',{'acteur':form,'dash':dash,'firstname':firstname} )



def galerie(request):
  user = User.objects.all()
  if request.user.username == 'admin':
    dash = 'active'
  else:
    dash = 'disabled'
  return render(request,'gestion/galerie.html',{'dash':dash} )



def acteur_list(request):
  firstname = request.user.username
  details=''
  aff =''
  numero = 0
  user = User.objects.all()
  acteurs = Acteur.objects.all()
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    acteurs = Acteur.objects.filter(nom_acteur__icontains=item_name)
  paginator = Paginator(acteurs,6)
  page=request.GET.get('page')
  acteurs = paginator.get_page(page)
  acteurs_list = []
  for acteur in acteurs:
    if acteur.valide == 1 or acteur.valide ==None or request.user.username=='admin':
      aff =True
      
    else:
      aff =False
      
    numero += 1
    if request.user.username=='admin':
      details = True
    else:
      details = False
    acteurs_list.append({"acteur": acteur,"numero":numero,'aff': aff})
   
  return render(request, "gestion/acteur_list.html", {"list": acteurs_list,"it" :acteurs,'details':details,'firstname':firstname})



def acteur_details(request,  pk ):
  firstname = request.user.username
  delete = ''
  user = User.objects.all()
  if request.user.username == 'admin':
    dash ='active'
    delete = True
  else :
    dash='disabled'
    delete =False
  usernom = False
  acteur = get_object_or_404(Acteur, pk=pk)
  recherche_emploi = acteur.recherche_emploi_set.all()
  communication  = acteur.communication_set.all()
  visite_sante = acteur.visite_set.all()
  visite_pharma = acteur.visiter_pharma_set.all()
  
    
    
  context ={
      'acteur': acteur,
      'recherche_emploi':recherche_emploi,
      'communication':communication,
      'visite_centresante ':visite_sante ,
      'visite_pharma ':visite_pharma,
      'dash':dash,
      'delete': delete ,
      'firstname':firstname     
    }
    
  return render(request, "gestion/acteur_details.html", context)


def acteur_edit(request, pk=None):
  valide=''
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
       dash = 'active'
       valide =True
  else:
       dash = 'disabled'
       valide =False
  hum = False
  if pk is not None:
    acteur = get_object_or_404(Acteur, pk=pk)
    
  else:
    acteur = None
      
  if request.method == "POST":
    if request.user.username == 'admin':
       form = ActeurForm(request.POST, instance=acteur)
    else:
      form= guessActeurForm(request.POST, instance=acteur)
    if form.is_valid():
      updated_acteur = form.save()
      actor  = Acteur.objects.all()
      for item in actor:
        if item.valide == 1 and request.user.username=='admin':
          item.statut ='ok'
          item.save()
        else:
          item.statut = 'non'
          item.save()
      if acteur is None:
        messages.success(request, "Acteur  \"{}\" a été crée.".format(updated_acteur.nom_cateur))
        
      else:
        messages.success(request, "Acteur \"{}\" a été mis à jour.".format(updated_acteur.nom_acteur ))
        return redirect("acteur_list")

     
  else:
    if request.user.username == 'admin':
      form = ActeurForm(instance=acteur)
    else:
      form= guessActeurForm(instance=acteur)
    hum= True
    return render(request,"gestion/acteurform.html",{"form": form,'dash':dash,'valide':valide,'firstname':firstname})
  return render(request, "gestion/acteurform.html",
                  {"form": form, "instance": hum, "model_type": "Acteur",'dash':dash,'valide':valide,'firstname':firstname})


def acteur_delete(request, pk=None):
  hum = False
  if pk is not None:
    acteur = get_object_or_404(Acteur, pk=pk)
    ad = acteur.id
    acteur.delete()
    messages.success(request, f"L'Acteur  {acteur.nom_acteur} numero {ad} a été supprimé.")
    return redirect("acteur_list")
   
  return render(request, "gestion/acteur_list.html")
                  




# fonctionnalités Pharmacie

def services_pharmacie(request):
  user = User.objects.all()
  firstname = request.user.username
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  
  form = PharmacieForm(instance=None)
  return render(request,'gestion/services_pharmacies.html',{'acteur':form,'dash':dash,'firstname':firstname})

  

def pharmacie_list(request):
  user = User.objects.all()
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  pagination_number =6
  numero = 0
  pharmacie = Pharmacie.objects.all()
  paginator = Paginator(pharmacie,pagination_number)
  page=request.GET.get('page')
  pharmacies = paginator.get_page(page)
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    pharmacie = Pharmacie.objects.filter(libele_pharmacie__icontains=item_name)
    pagination_number =20
    paginator = Paginator(pharmacie,pagination_number)
  pharmacies_list = []
  for item in pharmacie:
    numero += 1
    pharmacies_list.append({"pharmacie": item,"numero":numero})
   
  return render(request, "gestion/pharmacie_list.html", {"list": pharmacies_list,"it" :pharmacies,'dash':dash})


def pharmacie_edit(request, pk=None):
  user = User.objects.all()
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  hum = False
  if pk is not None:
    pharmacie = get_object_or_404(Pharmacie, pk=pk)
    
  else:
    pharmacie = None
      
  if request.method == "POST":
    if request.user.username == 'admin':
       form = PharmacieForm(request.POST, instance=pharmacie)
    else:
      form= guessPharmacieForm(request.POST, instance=pharmacie)
   
    if form.is_valid():
      updated_pharmacie = form.save()
      if pharmacie is None:
        messages.success(request, "La Pharmacie   \"{}\" a été ajouté.".format(updated_pharmacie))
        mail_admins(" Ajout de Pharmacie","la pharmacie \"{}\"a ete crée, à VALIDER".format(updated_pharmacie))
    
      else:
        messages.success(request, "la Pharmacie\"{}\" a été mis à jour.".format(updated_pharmacie))
        
        return redirect("pharmacie_list")

     
  else:
    if request.user.username == 'admin':
       form = PharmacieForm(instance=pharmacie)
    else:
      form= guessPharmacieForm(instance=pharmacie)
      hum= True
    
  
    return render(request,"gestion/pharmacieform.html",{"form": form,'dash':dash})
  return render(request, "gestion/pharmacieform.html",
                  {"form": form, "instance": hum, "model_type": "Pharmacie",'dash':dash})
  
 
def pharmacie_details(request,  pk ):
  temps =True
  delete = False
  user = User.objects.all()
 
  if request.user.username == 'admin':
    delete = True
  else :
    delete =False
  pharmacie = get_object_or_404(Pharmacie, pk=pk)
  #acteur = pharmacie.acteur_set.all()
  if pharmacie.garde == 1:
    garde = True
  else:
    garde = False
    
  temps_visite = pharmacie.visiter_pharma_set.all()
  if temps_visite == "":
    temps = False
  context ={
      'pharmacie': pharmacie,
      
      'temps_visite':temps_visite,
      'times':temps,
      'delete':delete,
      'garde':garde
           }
    
  return render(request, "gestion/pharmacie_details.html", context) 
 
 
 
def pharmacie_delete(request, pk=None):
  hum = False
  if pk is not None:
    pharmacie = get_object_or_404(Pharmacie, pk=pk)
    ad = pharmacie.id
    pharmacie.delete()
    messages.success(request, f"La pharmacie {pharmacie.libele_pharmacie} numero {ad} a été supprimé.")
    return redirect("pharmacie_list")
   
  return render(request, "gestion/pharmacie_list.html")
                  

 
   


# fonctionnalités naissance

def naissance_list(request):
  aff =''
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
       dash = 'active'
       delete = True
  else:
    delete = False
    dash = 'disabled'
    
 
    
  pagination_number =6
  naissance  = Naissance.objects.all()
  paginator = Paginator(naissance,pagination_number)
  page=request.GET.get('page')
  naissances= paginator.get_page(page)
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    naissance = Naissance.objects.filter(nom_nouveau_ne__icontains=item_name)
    pagination_number =20
    paginator = Paginator(naissance,pagination_number)
  naissances_li = []
  for item in naissance:
    if item.valide == 1 or item.valide ==None or request.user.username=='admin':
      aff =True

    else:
      aff =False
    
    
         
    naissances_li.append({"naissance": item,'aff': aff})
      
   
  return render(request, "gestion/naissance_list.html", {"list": naissances_li,"it" :naissances,'dash':dash,'delete':delete,'firstname':firstname })



def naissance_details(request,  pk ):
  delete = False
  user = User.objects.all()
  if request.user.username == 'admin':
    dash='active'
    delete = True
  else :
    dash='disabled'
    delete =False
  usernom = False
  naissance = get_object_or_404(Naissance, pk=pk)
  centre_sante = naissance.enregistrer_nais_set.all()
  
    
  context ={
      'naissance': naissance,
      'centre_sante':centre_sante,
      'dash':dash,
      'delete':delete      
    }
  return render(request, "gestion/naissance_details.html", context)
  

  
def services_naissance(request):
  user = User.objects.all()
  firstname = request.user.username
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  form = NaissanceForm(instance=None)
  return render(request,'gestion/services_naissance.html',{'naissance':form,'dash':dash,'firstname':firstname})



def naissance_edit(request, pk=None):
  valide=''
  user = User.objects.all()
   
  firstname = request.user.username
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  hum = False
  if pk is not None:
    naissance = get_object_or_404(Naissance, pk=pk)
    
  else:
    naissance = None
      
  if request.method == "POST":
    if request.user.username == 'admin':
      form = NaissanceForm(request.POST, instance=naissance)
    else:
      form= GuessNaissanceForm(request.POST, instance=naissance)
    
    if form.is_valid():
      
      updated_naissance = form.save()
      naissances  = Naissance.objects.all()
      for item in naissances:
        if item.valide == 1 and request.user.username=='admin':
          item.statut ='ok'
        else:
          item.statut = 'non'
          item.valide == 0
          item.save()
      if naissance is None:
        messages.success(request, "Le nouveau née  \"{}\" a été ajouté.".format(updated_naissance.nom_nouveau_ne))
      else:
        messages.success(request, "Données \"{}\" a été mis à jour.".format(updated_naissance.nom_nouveau_ne))
        return redirect("naissance_list")
  else:
    if request.user.username == 'admin':
      form = NaissanceForm(instance=naissance)
    else:
      form=GuessNaissanceForm(instance=naissance)
        
    hum= True
    return render(request,"gestion/naissanceform.html",{"form": form,'dash':dash,'firstname':firstname})
  return render(request, "gestion/naissanceform.html",
                  {"form": form, "instance": hum, "model_type": "naissance",'dash':dash,'firstname':firstname})
  

def naissance_delete(request, pk=None):
  hum = False
  if pk is not None:
    naissance = get_object_or_404(Naissance, pk=pk)
    ad = naissance.id
    naissance.delete()
    messages.success(request, f"Le nouveau née {naissance.nom_nouveau_ne}  numero {ad} a été supprimé.")
    return redirect("naissance_list")
   
  return render(request, "gestion/naissance_list.html")





# fonctionnalités décès

def deces_list(request,pk=None):
  dece =''
  delete = False
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
       dash = 'active'
       delete = True
  else:
    delete = False
    dash = 'disabled'
  if pk is not None:
    dece = get_object_or_404(Deces, pk=pk)
  
  pagination_number =6
  deces  = Deces.objects.all()
  
  paginator = Paginator(deces,pagination_number)
  page=request.GET.get('page')
  deces_mix= paginator.get_page(page)
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    deces_mix = Deces.objects.filter(raison_deces__icontains=item_name)
    
    paginator = Paginator(deces_mix,6)
    
  deces_li = []
  for item in deces:
    if item.valide == 1 or item.valide ==None or request.user.username=='admin':
      aff =True
      item.statut ="ok"
      
    else:
      aff =False
      
    deces_li.append({"deces": item,'aff': aff})
   
  return render(request, "gestion/deces_list.html", {"list": deces_li,"it" :deces_mix,'dash':dash,'delete':delete,'deces':deces,'dece':dece,'firstname':firstname})



def deces_delete(request, pk=None):
  delete = False
  user = User.objects.all()
  if request.user.username == 'admin':
    dash = 'active'
    delete = True
  else:
    delete = False
  hum = False
  if pk is not None:
    deces = get_object_or_404(Deces, pk=pk)
    ad = deces.id
    deces.delete()
    messages.success(request, f"Le nouveau née {deces.defunt}  numero {ad} a été supprimé.")
    return render(request,"gestion/services_deces.html",{'dash':dash,'delete':delete})
   
  return render(request, "gestion/services_deces.html")


  
def services_deces(request):
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  form = NaissanceForm(instance=None)
  return render(request,'gestion/services_deces.html',{'deces':form,'dash':dash,'firstname': firstname})



def deces_edit(request, pk=None):
  valide=''
  user = User.objects.all()
  firstname=request.user.username
  deces=""
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  hum = False
  if pk is not None:
    deces = get_object_or_404(Deces, pk=pk)
    
  else:
    deces = None
      
  if request.method == "POST":
    if request.user.username == 'admin':
       form = DecesForm(request.POST, instance=deces)
    else:
      form= GuessDecesForm(request.POST, instance=deces)
    
    if form.is_valid():
      updated_deces = form.save()
      decess  = Deces.objects.all()
      for item in decess:
        if item.valide == 1 and request.user.username=='admin':
          item.statut ='ok'
          item.save()
        else:
          item.statut = 'non'
          item.save()
      if deces is None:
        messages.success(request, "Le nouveau décédé  \"{}\" a été ajouté.".format(updated_deces.defunt.nom_acteur))
      else:
        messages.success(request, "Données \"{}\" a été mis à jour.".format(updated_deces.defunt.nom_acteur))
        return redirect("deces_list")
  else:
    if request.user.username == 'admin':
      form = DecesForm(instance=deces)
    else:
      form= GuessDecesForm(instance=deces)
    
    hum= True
    return render(request,"gestion/decesform.html",{"form": form,'dash':dash,'firstname':firstname})
  return render(request, "gestion/decesform.html",
                  {"form": form, "instance": hum, "model_type": "deces",'dash':dash,'firstname':firstname})
  

# fonctionnalités recherceh emploi

def services_recherce_emploi(request):
  user = User.objects.all()
  
  firstname= request.user.username
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  
  form = Recherche_emploiForm(instance=None)
  return render(request,'gestion/services_recherche_emploi.html',{'emploi':form,'dash':dash,'firstname':firstname})





def recherche_emploi_list(request,pk=None):
  reche =''
  delete = False
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
       dash = 'active'
       delete = True
  else:
    delete = False
    dash = 'disabled'
  if pk is not None:
    reche = get_object_or_404(Recherche_emploi, pk=pk)
  
  pagination_number =6
  recherche_emploi  = Recherche_emploi.objects.all()
  paginator = Paginator(recherche_emploi,pagination_number)
  page=request.GET.get('page')
  recherche_mix= paginator.get_page(page)
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    recherche_emploi = Recherche_emploi.objects.filter(services__icontains=item_name)
    pagination_number =20
    paginator = Paginator(recherche_emploi,pagination_number)
    
  recherche_li = []
  for item in recherche_emploi :
   
    if item.valide == 1 or item.valide ==None or request.user.username=='admin':
      aff =True
      item.statut = 'ok'
    else:
      aff = False
      item.statut ='non'
    if request.user.username=='admin':
      details = True
    else:
      details = False
      
    recherche_li.append({"recherche": item,'aff':aff})
 
  return render(request, "gestion/recherche_emploi_list.html", {"list": recherche_li,"it" :recherche_mix,'dash':dash,'delete':delete, 'reche':reche,'firstname':firstname})


def recherche_emploi_edit(request, pk=None):
  updated_recherche=""
  user = User.objects.all()
  firstname = request.user.username
  deces=""
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  hum = False
  if pk is not None:
    recherce_emploi = get_object_or_404(Recherche_emploi, pk=pk)
    
  else:
    recherce_emploi = None
      
  if request.method == "POST":
    form = Recherche_emploiForm(request.POST, files= request.FILES, instance=recherce_emploi)
    if form.is_valid():
      updated_recherche = form.save()
      recherce_emplois = Recherche_emploi.objects.all()
      for item in recherce_emplois:
        if item.valide == 1 and request.user.username=='admin':
          item.statut ='ok'
          item.save()
        else:
          item.statut = 'non'
          item.save()
      if recherce_emploi is None:
        messages.success(request, "La nouvelle demande \"{}\" a été ajouté.".format(updated_recherche.acteur_emploi.nom_acteur))
      else:
        messages.success(request, "La démande  \"{}\" a été mis à jour.".format(updated_recherche.acteur_emploi.nom_acteur))
        return redirect("recherche_emploi_list")
  else:
    if request.user.username == 'admin':
      form = Recherche_emploiForm(instance=recherce_emploi)
    else:
      form= GuessrechercheForm(instance=recherce_emploi)
    
  
   
    hum= True
    return render(request,"gestion/recherche_emploiform.html",{"form": form,'dash':dash,'firstname':firstname})
  return render(request, "gestion/recherche_emploiform.html",
                  {"form": form, "instance": hum, "model_type": "recherche_emploi",'dash': dash,'firstname':firstname  })  
  
  
def recherche_delete(request, pk=None):
  delete = False
  user = User.objects.all()
  if request.user.username == 'admin':
    dash = 'active'
    delete = True
  else:
    delete = False
    hum = False
  if pk is not None:
    recherche_emploi = get_object_or_404(Recherche_emploi, pk=pk)
    ad = recherche_emploi.id
    recherche_emploi.delete()
    messages.success(request, f"La demande d'emploi {recherche_emploi.services}  numero {ad} a été supprimée.")
    return render(request,"gestion/services_recherche_emploi.html",{'dash':dash,'delete':delete})
   
  return render(request, "gestion/services_recherche_emploi.html")



# fonctionnalités mouvement


def services_mouvement(request):
  user = User.objects.all()
  firstname= request.user.username
  if request.user.username == 'admin':
    dash = 'active'
  else:
    dash = 'disabled'
  
  return render(request,'gestion/services_mouvement.html',{'dash':dash,'firstname':firstname})



def mouvement_a_list(request,pk=None):
  reche =''
  delete = False
  user = User.objects.all()
  firstname = request.user.username
  if request.user.username == 'admin':
       dash = 'active'
       delete = True
  else:
    delete = False
    dash = 'disabled'
  if pk is not None:
    mouvement_a = get_object_or_404(Venant, pk=pk)
  
  pagination_number =6
  mouvement  = Venant.objects.all()
  paginator = Paginator(mouvement,pagination_number)
  page=request.GET.get('page')
  recherche_mix= paginator.get_page(page)
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    recherche_mix = Venant.objects.filter(nom__icontains=item_name)
    pagination_number =20
    paginator = Paginator(recherche_mix,pagination_number)
    
  recherche_li = []
  for item in mouvement:
   
    if item.valide == 1 or item.valide ==None or request.user.username=='admin':
      aff =True
      item.statut = 'ok'
    else:
      aff = False
      item.statut ='non'
      
    recherche_li.append({"mouvement": item,'aff':aff})
 
  return render(request, "gestion/mouvement_a.html", {"list": recherche_li,"it" :recherche_mix,'dash':dash,'delete':delete, 'reche':reche,'firstname':firstname})



def  amenageant_edit(request, pk=None):
  updated_venant=""
  user = User.objects.all()
  deces=""
  if request.user.username == 'admin':
       dash = 'active'
  else:
       dash = 'disabled'
  hum = False
  if pk is not None:
    amenageant= get_object_or_404(Venant, pk=pk)
    
  else:
    amenageant = None
      
  if request.method == "POST":
    form = VenantForm(request.POST, instance=amenageant)
    if form.is_valid():
      updated_venant = form.save()
      amenageants = Venant.objects.all()
      for item in amenageants:
        if item.valide == 1 and request.user.username=='admin':
          item.statut ='ok'
          item.save()
        else:
          item.statut = 'non'
          item.save()
      if amenageant is None:
        messages.success(request, "Le Nouvel Arrivant\"{}\" a été ajouté.".format(updated_venant.nom))
      else:
        messages.success(request, "Le Nouvel Arrivant \"{}\" a été mis à jour.".format(updated_venant.nom))
        return redirect("amenageant_list")
  else:
    if request.user.username == 'admin':
      form = VenantForm(instance=amenageant)
    else:
      form= GuessVenantForm(instance=amenageant)
      
   
    hum= True
    return render(request,"gestion/mouvement_aform.html",{"form": form,'dash':dash})
  return render(request, "gestion/mouvement_aform.html",
                  {"form": form, "instance": hum, "model_type": "Amenageant",'dash': dash  })  
  
  
  
def amenageant_delete(request, pk=None):
  delete = False
  user = User.objects.all()
  if request.user.username == 'admin':
    dash = 'active'
    delete = True
  else:
    delete = False
    hum = False
  if pk is not None:
    amenageant = get_object_or_404(Venant, pk=pk)
    ad = amenageant.id
    amenageant.delete()
    messages.success(request, f"La demande d'emploi {amenageant.nom}  numero {ad} a été supprimée.")
    return render(request,"gestion/services_mouvement.html",{'dash':dash,'delete':delete})
    
  return render(request, "gestion/services_mouvement.html")