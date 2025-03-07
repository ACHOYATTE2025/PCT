"""
URL configuration for PCT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
import account.views
import gestion.views
import dashboard.views
from gestion.admin import admin_site
from django.contrib.admin.apps import AdminConfig
from django.conf import settings
from xml.dom.minidom import Document
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('allakroadmin/',admin_site.urls),
    path('', gestion.views.index),
    path('', dashboard.views.dashboard),
    path('',include('account.urls')),
    path('',include('gestion.urls')),
    path('',include('dashboard.urls'))
]  + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)


# styler la page admin
admin.site.site_header = "PROJET COMMUNAUTAIRE TUTORE"
admin.site.site_title = "GROUPE 01"
admin.site.index_title = " BIENVENUE"


