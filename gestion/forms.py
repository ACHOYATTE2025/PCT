from django import forms
from .models import Acteur, Pharmacie, Naissance, Deces, Recherche_emploi, Venant
from django.contrib.auth.models import User




choix = [
  (1,'valider'),
  (0,'non_valider')
]     

garde = [
  (1,'garde'),
  (0,'pas_de_garde')
]     

class ActeurForm(forms.ModelForm):
  class Meta:
    model = Acteur
    fields = ('nom_acteur','prenom_acteur','contact_acteur','email_acteur','nombre_enfants','statut_prof',
               'pays_naissance','situation_matrimoniale','nom_acteur','situation_matrimoniale','nationalité_acteur','competences_acteur','valide')
       
      
    widgets ={
      'nom_acteur': forms.TextInput(attrs={'class':"form-control"}),
      'prenom_acteur': forms.TextInput(attrs={'class':'form-control'}),
      'contact_acteur': forms.TextInput(attrs={'class':'form-control'}),
      'email_acteur': forms.EmailInput(attrs={'class':'form-control'}),
      'nombre_enfants': forms.TextInput(attrs={'class':'form-control'}),
      'statut_prof': forms.TextInput(attrs={'class':'form-control'}),
      'pays_naissance': forms.TextInput(attrs={'class':'form-control'}),
      'situation_matrimoniale': forms.TextInput(attrs={'class':'form-control'}),
      'nom_acteur': forms.TextInput(attrs={'class':'form-control'}),
      'situation_matrimoniale': forms.TextInput(attrs={'class':'form-control'}),
      'nationalité_acteur': forms.TextInput(attrs={'class':'form-control'}),
      'competences_acteur':forms.TextInput(attrs={'class':'form-control'}),
       'valide':forms.Select(choices=choix,attrs={'class':'form-control'})
     
    }
    
class guessActeurForm(ActeurForm):
  def __init__(self, *args,**kwargs):
    super(guessActeurForm, self).__init__(*args, **kwargs)
    self.fields.pop('valide')
    


class PharmacieForm(forms.ModelForm):
  class Meta:
    model = Pharmacie
    fields =('libele_pharmacie','emplacement_pharmacie','garde')
   
    widgets ={
      'libele_pharmacie': forms.TextInput(attrs={'class':"form-control"}),
      'emplacement_pharmacie': forms.TextInput(attrs={'class':'form-control'}),
      'garde': forms.Select(choices=garde,attrs={'class':"form-control"})
    }
    
    
class guessPharmacieForm(PharmacieForm):
  def __init__(self, *args,**kwargs):
    super(guessPharmacieForm, self).__init__(*args, **kwargs)
    self.fields.pop('garde')
    

class NaissanceForm(forms.ModelForm):
  class Meta:
    model = Naissance
    fields = ('nom_nouveau_ne','genre','date_naissance_enfant','mode_naissance','nom_pere', 'nom_mere','lieu_habitation','valide')
   
    widgets ={
      'nom_nouveau_ne': forms.TextInput(attrs={'class':"form-control"}),
      'genre': forms.TextInput(attrs={'class':'form-control'}),
      'date_naissance_enfant': forms.DateInput(attrs={'class':'form-control'}),
      'mode_naissance': forms.TextInput(attrs={'class':"form-control"}),      
      'nom_pere': forms.TextInput(attrs={'class':'form-control'}),
      'nom_mere': forms.TextInput(attrs={'class':'form-control'}),
      'lieu_habitation': forms.TextInput(attrs={'class':'form-control'}),
      'valide':forms.Select(choices=choix,attrs={'class':'form-control'})
    }
    
    
class GuessNaissanceForm(NaissanceForm):
  def __init__(self, *args,**kwargs):
    super(GuessNaissanceForm, self).__init__(*args, **kwargs)
    self.fields.pop('valide')




class DecesForm(forms.ModelForm):
  class Meta:
    model = Deces
    fields = ('date_naissance_deces','date_deces', 'mode_deces','raison_deces','parent_referant','lieu_deces','defunt','valide')
    
   
    widgets ={
      
      'date_naissance_deces': forms.TextInput(attrs={'class':"form-control"}),
      'date_deces': forms.DateInput(attrs={'class':'form-control'}),
      'mode_deces': forms.TextInput(attrs={'class':'form-control'}),
      'raison_deces': forms.TextInput(attrs={'class':"form-control"}),      
      'parent_referant': forms.TextInput(attrs={'class':'form-control'}),
      'lieu_deces': forms.TextInput(attrs={'class':'form-control'}) ,
      'defunt': forms.Select(choices=choix,attrs={'class':'form-control'}),
      'valide':forms.Select(choices=choix,attrs={'class':'form-control'})
          
    }
    
  
  

class GuessDecesForm(DecesForm):
  def __init__(self, *args,**kwargs):
    super(GuessDecesForm, self).__init__(*args, **kwargs)
    self.fields['valide'].required =False
    self.fields.pop('valide')




class Recherche_emploiForm(forms.ModelForm):
  class Meta:
    model = Recherche_emploi
    fields = ('photo','services','message','acteur_emploi','valide')
         
     
    widgets ={
      'photo': forms.FileInput(attrs={'class':"form-control"}),
      'services': forms.TextInput(attrs={'class':'form-control'}), 
      'message': forms.Textarea(attrs={'class':'form-control'}),
      'acteur_emploi': forms.Select(attrs={'class':'form-control'}),
      'valide':forms.Select(choices=choix,attrs={'class':'form-control'})
                
    }
    
class GuessrechercheForm(Recherche_emploiForm):
  def __init__(self, *args,**kwargs):
    super(GuessrechercheForm, self).__init__(*args, **kwargs)
    self.fields['valide'].required =False
    self.fields.pop('valide')
    
    




# Amenageant


class VenantForm(forms.ModelForm):
 
  class Meta:
    model = Venant
    fields = ('nom','prenoms','genre','fonction','date_naissance','contact','email','nationalite','valide')
    
      
     
    widgets ={
      'nom': forms.TextInput(attrs={'class':"form-control"}),
      'prenoms': forms.TextInput(attrs={'class':'form-control'}), 
      'genre': forms.Select(attrs={'class':'form-control'}),
      'fonction':forms.TextInput(attrs={'class':'form-control'}),
      'date_naissance':forms.DateInput(attrs={'class':'form-control'}),
      'contact':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
      'nationalite':forms.TextInput(attrs={'class':'form-control'}),
      'valide': forms.Select(choices=choix,attrs={'class':'form-control'})
                
    }
    
class GuessVenantForm(VenantForm):
  def __init__(self, *args,**kwargs):
    super(GuessVenantForm, self).__init__(*args, **kwargs)
    self.fields['valide'].required= False
    self.fields.pop('valide')
    
    
    
