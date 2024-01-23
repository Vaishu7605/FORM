from django.shortcuts import render,redirect
from .models import *
from .form import *

# Create your views here.


def create(request):
    a=clientform()
    b=register.objects.all()
    if request.method=='POST':
        a=clientform(request.POST)
        if a.is_valid():
            a.save()
        else:
            print('invalid input')
    else:
        a=clientform
    return render(request,'signup.html',{'frm':a,'data':b})

def update(request,id):
    c=register.objects.get(id=id)
    d=register.objects.all()
    e=clientform(instance=c)

    if request.method=='POST':
        a=clientform(request.POST,instance=c)
        if a.is_valid():
            a.save()
            return redirect('create')
        else:pass
    else:pass
    return render(request,'signup.html',{'frm':e,'data':d})

def delete(request,id):
    c=register.objects.get(id=id)
    c.delete()
    return redirect('create')


