from django.contrib import admin
from django.contrib.admin import AdminSite
from gestion.models import*

# Register your models here.
class ALLAKROAdminSite(AdminSite):
    title_header = 'ALLAKRO Admin'
    site_header = 'allakro administration'
    index_title = 'ALLAKRO site admin'
    
admin_site = ALLAKROAdminSite(name='ALLAKRO')





class ActeurAdmin(admin.ModelAdmin):
    list_display = ('nom_acteur', 'nationalité_acteur','contact_acteur')
    list_filter =('nom_acteur',)
    search_fields = ('nom_acteur', 'nationalité_acteur')

admin_site.register(visite)
admin_site.register(Deces)
admin_site.register(Recherche_emploi)
admin_site.register(Communication)
admin_site.register(Posseder_outils)
admin_site.register(Centre_sante)
admin_site.register(Naissance)
admin_site.register(Enregistrer_nais)
admin_site.register(Maladie_Epidemie)
admin_site.register(Enregistrer_epimal)
admin_site.register(Services_sante)
admin_site.register(Abriter)
admin_site.register(Traiter)
admin_site.register(Acteur, ActeurAdmin)
admin_site.register(Venant)



    

admin.site.register(visite)
admin.site.register(Deces)
admin.site.register(Recherche_emploi)
admin.site.register(Communication)
admin.site.register(Posseder_outils)
admin.site.register(Centre_sante)
admin.site.register(Naissance)
admin.site.register(Enregistrer_nais)
admin.site.register(Maladie_Epidemie)
admin.site.register(Enregistrer_epimal)
admin.site.register(Services_sante)
admin.site.register(Abriter)
admin.site.register(Traiter)
admin.site.register(Pharmacie)
admin.site.register(Visiter_pharma)
admin.site.register(Periode_garde)
admin.site.register(Venant)

