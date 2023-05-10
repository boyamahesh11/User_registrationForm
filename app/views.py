from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)

    return render(request,'home.html')

def registration(request):
    Ufo=UserForm()
    Pfo=ProfileForm()
    d={'Ufo':Ufo,'Pfo':Pfo}
    
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            nuo=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            nuo.set_password(password)
            nuo.save()

            npo=pfd.save(commit=False)
            npo.user_name=nuo
            npo.save()

            send_mail('Registration',
                      "sucessfully Registration is done", 
                      "maheshmahi8039@gmail.com",
                      [nuo.email],
                      fail_silently=False)

            return HttpResponse('Registration is sucessfull!!')
        else:
            return HttpResponse('Not valid')

    return render(request,'registration.html',d)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid username or password')
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def display_profile(request):
    username=request.session.get('username')
    uo=User.objects.get(username=username)
    po=Profile.objects.get(user_name=uo)

    d={'uo':uo,'po':po}
    return render(request,'display_profile.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        uo=User.objects.get(username=username)
        uo.set_password(pw)
        uo.save()
        return HttpResponse('change password sucessfully!!!')
    return render(request,'change_password.html')

@login_required
def forgot_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        return HttpResponse('forgot_password is sucessfully!!')
        
    return render(request,'forgot_password.html')

    


