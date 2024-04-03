from itertools import chain
from  django . shortcuts  import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Q




def signup(request):
 try:
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        user_model = User.objects.get(username=fnm)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        if my_user is not None:
            login(request,my_user)
            return redirect('/')
        return redirect('/loginn')
    
        
 except:
        invalid="User already exists"
        return render(request, 'signup.html',{'invalid':invalid})
  
    
 return render(request, 'signup.html')
        
     
        
        
        
        
    

def loginn(request):
 
  if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/')
        
 
        invalid="Invalid Credentials"
        return render(request, 'loginn.html',{'invalid':invalid})
               
  return render(request, 'loginn.html')

@login_required(login_url='/loginn')
def logoutt(request):
    logout(request)
    return redirect('/loginn')



@login_required(login_url='/loginn')
def home(request):
    name = request.user.username
    return render(request, 'index.html', {'name':name})
    
    








