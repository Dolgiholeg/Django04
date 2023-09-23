from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    return render(req,'index.html')

from .forms import *
def def1(req):
    print(1)#чек поинт
    if req.method == "POST":
        print(2)  # чек поинт
        anketa = UserformComment(req.POST)
        if anketa.is_valid():
            print(3)  # чек поинт
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['email']
            k3 = anketa.cleaned_data['com']
            print(k1, k2, k3)
        else:
            print('не получилось')
    else:
        anketa = UserformComment()
    data = {'form': anketa}
    return render(req, 'forform.html', context=data)

def def2(req):
    print(1)#чек поинт
    if req.method == "POST":
        print(2)  # чек поинт
        anketa = UserformErrors(req.POST)
        if anketa.is_valid():
            print('ok')
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['num']
            k3 = anketa.cleaned_data['agree']
            print(k1, k2, k3)
            return redirect('home')
        else:
            print('неok')
            print(anketa.errors)
    else:
        anketa = UserformErrors()
    data = {'form': anketa}
    return render(req, 'forform.html', context=data)

def def3(req):
    print(1)#чек поинт
    if req.method == "POST":
        print(2)  # чек поинт
        anketa = UserformValidator(req.POST)
        if anketa.is_valid():
            print('ok')
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['cod']
            k3 = anketa.cleaned_data['tel']
            print(k1, k2, k3)
            return redirect('home')

    else:
        anketa = UserformValidator()
    data = {'form': anketa}
    return render(req, 'forform.html', context=data)

def def4(req):

    if req.method =="POST":
        anketa = Water(req.POST)
        if anketa.is_valid():
            name = req.POST.get('name')
            surname = req.POST.get('surname')
            email = req.POST.get('email')
            tel = req.POST.get('tel')
            adres = req.POST.get('adres')
            period = req.POST.get('period')
            volume = req.POST.get('volume')
            data = {'name': name, 'surname': surname, 'email': email, 'tel': tel, 'adres': adres, 'period': period, 'volume': volume}
            return render(req, 'water.html', context=data)
        else:
            data = {'form': anketa}
            return render(req, 'forform.html',data)
    else:
        anketa = Water()
        data = {'form': anketa}
        return render(req, 'forform.html', context=data)

