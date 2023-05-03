from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

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
            return HttpResponse('Registration is sucessfull!!')
        else:
            return HttpResponse('Not valid')



    return render(request,'registration.html',d)


    


