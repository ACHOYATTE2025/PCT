from django.db import models
from django.contrib.admin import AdminSite

# Create your models here.




# Entité Acteur
class Acteur(models.Model):
  class Genreacteur(models.TextChoices):
    MASCULIN = "MASCULIN", "Masculin"
    FEMININ = "FEMININ", "Feminin"
  class Valideracteur(models.TextChoices):
    VALIDER = 'valider'
    NON_VALIDER = 'non_valider'
  nom_acteur = models.CharField(default='inconnu',max_length=20,verbose_name="nom de l'acteur" )
  prenom_acteur = models.CharField(default='inconnu',max_length=30,verbose_name="prenoms de l'acteur")
  genre_acteur= models.CharField(default='inconnu',max_length=20,choices=Genreacteur.choices, verbose_name="genre de l'acteur")
  contact_acteur = models.CharField(default='inconnu',max_length=20,verbose_name="contact de l'acteur")
  provenance = models.CharField(default='inconnu',max_length=20,verbose_name="provenance de l'acteur")
  email_acteur =models.EmailField(default='',verbose_name="email de l'acteur")
  age_acteur = models.CharField(default='',max_length=20,verbose_name="age del'acteur")
  nombre_enfants = models.CharField(default='inconnu',max_length=20,verbose_name="nombre enfants de l'acteur")
  statut_prof = models.CharField(default='inconnu',max_length=50,verbose_name="metier de l'acteur")
  pays_naissance = models.CharField(default='inconnu',max_length=20,verbose_name="pays de naissance")
  situation_matrimoniale = models.CharField(default='inconnu',max_length=20,verbose_name="situation_matrimoniale")
  nationalité_acteur = models.CharField(default='inconnu',max_length=20,verbose_name="nationalité de l'acteur")
  competences_acteur = models.CharField(default='inconnu',max_length=50,verbose_name="competences de l'acteur")
  valide = models.BooleanField(default=1,verbose_name='valider la personne')
  statut = models.CharField(max_length=3,default= 'ok',verbose_name='choix')
  

  def __str__(self):
    
    return self.nom_acteur + ' -- ' +str(self.contact_acteur)
  
class visite(models.Model):
 
  date_visite = models.DateField(help_text='date de la visite')
  nom_acteur = models.ForeignKey('Acteur',max_length=20,on_delete= models.CASCADE, help_text='nom acteur')
  centre_sante_visite = models.ForeignKey('Centre_sante',max_length=20,on_delete= models.CASCADE, help_text="centre de santé visité par l'acteur")
 
 
# information Décès

class Deces(models.Model):
  class Validerdeces(models.TextChoices):
    VALIDER = 'valider'
    NON_VALIDER = 'non_valider'
  parent_referant = models.CharField(max_length=20,verbose_name="parent  de l'acteur decédé")
  date_naissance_deces =  models.DateField(verbose_name="date de naissance de décès de l'acteur ")
  date_deces =  models.DateField(verbose_name="date  de décès de l'acteur ")
  mode_deces =  models.CharField(max_length=20,verbose_name="mode de décès de l'acteur ")
  raison_deces =  models.CharField(max_length=20,verbose_name="raison de décès de l'acteur ")
  parent_referant = models.CharField(max_length=20,verbose_name="parent  de l'acteur decédé")
  lieu_deces = models.CharField(max_length=20,verbose_name="lieu du deces de l'acteur")
  defunt = models.OneToOneField('Acteur',on_delete=models.CASCADE)
  valide = models.BooleanField(default=0,verbose_name='valider la personne')
  statut = models.CharField(max_length=3,default= 'non',verbose_name='choix')
  
  
  
 
  def _str_(self):
    return f'{self.date_deces}---{self.lieu_deces}'       
  
 
# Recherche emploi
class Recherche_emploi(models.Model):
  class Valide_emploi(models.TextChoices):
    VALIDER = 'valider'
    NON_VALIDER = 'non_valider'
  photo = models.ImageField(upload_to="photos", blank=True, null=True)
  services = models.CharField(max_length=80,verbose_name=" services proposés par l'acteur")
  message = models.TextField(verbose_name='Message au public')
  acteur_emploi = models.ForeignKey('Acteur', on_delete= models.CASCADE)
  valide = models.BooleanField(default=0,verbose_name='valider la personne')
  statut = models.CharField(max_length=3,verbose_name='choix')
  
  
  def _str_(self):
     return "{}---{}".format(self.titre_emploi, self.emploi_acteur)
   

# outils communication

class Communication(models.Model):
  libele_comm = models.CharField(max_length=50,help_text="outils de communication de l'acteur")
  date_com = models.DateField(help_text="date d'acquisition de l'outil de l'acteur")
  acteur_com = models.ManyToManyField('Acteur', through='Posseder_outils')
  
  def _str_(self):
    return f'{self.libele_comm}---{self.date_com}'
  
class Posseder_outils(models.Model):
  com_acteur = models.ForeignKey('Acteur',on_delete= models.CASCADE, help_text="acteur possedant l'outil de communication")
  com_outils = models.ForeignKey('Communication',on_delete= models.CASCADE, help_text="outils de communication possédé par l'acteur")
  
  def _str_(self):
    return f'{ self.com_acteur}---{self.com_outils}'
 
# Groupe santé 
  
  
# centre de Santé
class Centre_sante(models.Model):
  libele_sante = models.CharField(max_length=20,help_text="nom du centre de santé")
  emplacement_sante = models.CharField(max_length=20,help_text="emplacement du centre de santé")
  nom_acteur_sante = models.ManyToManyField('Acteur',default="inconnu",through='Visite')
    
  def __str__(self):
    return "{}---{}".format(self.libele_sante, self.emplacement_sante)
  
  
# naissance  
class Naissance(models.Model):
  class Validernaissance(models.TextChoices):
    VALIDER = 'valider'
    NON_VALIDER = 'non_valider'
  class Genrenaissance(models.TextChoices):
        MASCULIN = "MASCULIN", "Masculin"
        FEMININ = "FEMININ", "Feminin"
  nom_nouveau_ne =  models.CharField(max_length=40,verbose_name="nom du nouveau née")
  genre =  models.CharField(max_length=20,choices=Genrenaissance.choices,verbose_name="genre du nouveau née")
  date_naissance_enfant = models.DateField(verbose_name="date de naissance enfant")
  mode_naissance =  models.CharField(max_length=20,verbose_name="nom de l'hopital")
  nom_pere =  models.CharField(max_length=30,verbose_name="nom du père")
  nom_mere =  models.CharField(max_length=30,verbose_name="nom de la mère")
  lieu_habitation =  models.CharField(max_length=20,verbose_name="lieu d'habitation des parents")
  centre_sante_naissance = models.ManyToManyField('Centre_sante', through="Enregistrer_nais")
  valide = models.BooleanField(default=0,verbose_name='valider la personne')
  statut = models.CharField(max_length=3,default= 'non',verbose_name='choix')

  def __str__(self):
    return "{}---{}".format(self.nom_nouveau_ne, self.genre)
  

class Enregistrer_nais(models.Model):
  centre_sante = models.ForeignKey('Centre_sante',on_delete = models.CASCADE)
  naissance_eng = models.ForeignKey('Naissance',on_delete = models.CASCADE)
  nombre_naissance = models.CharField(max_length=20,help_text='nombre de maissace')
  
# Maladie ,épidemie 
class Maladie_Epidemie(models.Model):
  Libele_maladie = models.CharField(max_length=20,help_text="titre des épidemies")
  nombre_morts = models.IntegerField(help_text="nombre de morts")
  centre_sante_epimal = models.ManyToManyField('Centre_sante',through="Enregistrer_epimal")
  
  def __str__(self):
    return "{}--- Nombre de décès : {}".format(self.Libele_maladie, self.nombre_morts)
  
  
class Enregistrer_epimal(models.Model):
  centre_sante = models.ForeignKey('Centre_sante',on_delete = models.CASCADE)
  maladie_epidemie = models.ForeignKey('Maladie_Epidemie',on_delete = models.CASCADE)
  epidemie_ou_pas  = models.BooleanField(help_text="présence d'épidemies oui ou nom")
   


# services santé  
class Services_sante(models.Model):
  Libele_services = models.CharField(max_length=20,help_text="nom du service")
  centre_sante_c = models.ManyToManyField('Centre_sante', through='Abriter')
  maladie_epidemie = models.ManyToManyField('Maladie_Epidemie', through="Traiter" )
  
  def __str__(self):
    return "{}---{}".format(self.Libele_services, self.centre_sante_c)
  

class Abriter(models.Model):
  libele_centresante =  models.ForeignKey('Centre_sante',on_delete = models.CASCADE)
  Libele_servicessante =  models.ForeignKey('Services_sante',on_delete = models.CASCADE) 

class Traiter(models.Model):
  libele_malepitraite = models.ForeignKey('Maladie_Epidemie',on_delete = models.CASCADE)
  libele_servicesante = models.ForeignKey('Services_sante',on_delete = models.CASCADE)
  

# Groupe Pharmacie

class Pharmacie(models.Model):
  libele_pharmacie = models.CharField(max_length=20, verbose_name='nom de la pharmarcie')
  emplacement_pharmacie = models.CharField(max_length=20, verbose_name='emplacement de la pharmarcie')
  acteur_pharma = models.ManyToManyField('Acteur', through='Visiter_pharma')
  garde = models.BooleanField(default=0,verbose_name='valider la personne')
  
  
  def __str__(self):
    return "{}---{}".format(self.libele_pharmacie, self.emplacement_pharmacie)
    

class Visiter_pharma(models.Model):
  somme_depense =  models.IntegerField(verbose_name='montant depensant')
  nom_acteur_visiste = models.ForeignKey('Acteur',on_delete= models.CASCADE)
  pharmacie_visite = models.ForeignKey('Pharmacie' ,on_delete= models.CASCADE,help_text='nom de la pharmarcie visite')
  temps_visite = models.DateTimeField(help_text='la date et le temps de la visite')
  
class Periode_garde(models.Model):
  periode = models.DateField(help_text='date de garde')
  pharmacie_de_garde = models.ForeignKey('Pharmacie',help_text='pharmacie de garde', on_delete=models.CASCADE)
  

# MOUVEMENT DES ACTEURS D'ALLAKRO

class Venant(models.Model):
  class Validervenant(models.TextChoices):
    VALIDER = 'valider'
    NON_VALIDER = 'non_valider'
  class Amena(models.TextChoices):
    FEMININ = 'feminin'
    MASCULIN ='masculin'
  nom = models.CharField(max_length=20, verbose_name='Nom ')
  prenoms = models.CharField(max_length=30, verbose_name='Prenoms')
  genre = models.CharField(max_length=20,choices=Amena.choices, verbose_name='Genre')
  fonction =models.CharField(max_length=30, verbose_name='Fonction')
  date_naissance= models.DateField( verbose_name='Date de naissance')
  contact= models.CharField(max_length=20, verbose_name='Contact')
  email= models.EmailField( verbose_name='Email')
  nationalite= models.CharField(max_length=20, verbose_name='Nationalite')
  valide = models.BooleanField(default=0,verbose_name='valider la personne')
  statut = models.CharField(max_length=3,default= 'non',verbose_name='choix')
 
 
  def __str__(self):
    return "{}---{}".format(self.nom, self.email)