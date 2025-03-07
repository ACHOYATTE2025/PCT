from django.shortcuts import render,  get_object_or_404,redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def sign_up(request):
  
  sonic = ''
  dash = ''
  error =True
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate( username=username, password=password)
    if user is not None:
      login(request, user)
      firstname = user.first_name
      user = User.objects.all()
      if request.user.username == 'admin':
        dash = 'active'
      else:
        dash = 'disabled'
        sonic = False
             
      near = {"firstname":firstname,
              "dash":dash,
              'sonic':sonic
              }
      return render(request, 'base1.html',near)
  
    else:
      messages.error(request, ' Mauvaise Authentification')
      
  
  return render(request, 'account/login.html',{"error" : error})


def register(request):
  mess = True
  error = False
  message = ""
  username =''
     
  if request.method == "POST":
    password_1 = request.POST['password']
    password_2 = request.POST['confirm_password']
     
    # checking of password   and  get value
    if password_1 == password_2:
      username = request.POST['username']
      name_1 = request.POST['first_name']
      name_2 = request.POST['last_name']
      email = request.POST['email']
      password = request.POST['password']
      
       
      # Exist User
      user = User.objects.filter( username=username).first()
      user_mix = User.objects.filter( username=username,email=email).first()
      
      if user or user_mix:
        error = True
        messages.error(request, f"CET UTILISATEUR {username} AVEC l'EMAIL : {email} EXISTE DEJA")
      elif not username.isalnum():
        messages.error(request,'VOTRE USERNAME DOIT ETRE ALPHANUMERIQUE')
      
      # register
      else:
        error= False
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name_1
        user.last_name = name_2
        user.save()
        messages.success(request, ' VOTRE INSCRIPTION EST VALIDEE')
        return render(request, 'account/login.html',{"error":error})
    else:
      error = True
      messages.error(request,"LES MOTS DE PASSE NE CONCORDENT PAS")
      
      #checking email
      try:
        validate_email(email)
      except:
        error= True
        message = "S'IL VOUS PLAÎT ENTREZ UN EMAIL VALIDE"
  
  data = {"error":error,
        "message":message}
 
  return render(request, 'account/login.html',data)



def log_out(request):
  messages.success(request,"BYE VOUS ÊTES DECONNECTE")
  logout(request)
  return render(request, 'base1.html')