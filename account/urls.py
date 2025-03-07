from django.urls import path
from . import views
import account.views


urlpatterns = [
    path('', views.login),
    path('home/', views.sign_up, name='home'),
    path('login/', views.sign_up, name='login'),
    path('logout/',views.log_out,name='log_out'),
    path('register/',views.register,name='register'),
]