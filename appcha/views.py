from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import * 
from django.db.models import Q
# Create your views here.

def home(request):
    if 'qidiruv' in request.GET:
        qidirish = request.GET['qidiruv']
        product = Main.objects.filter(Q(Q(name__icontains = qidirish)) | Q(name__icontains = qidirish))
    else:
        product = Main.objects.all()
    return render(request, 'index.html', {'product':product})

def add(request):
    form = MainForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = MainForm()
    return render(request, 'add.html', {'form':form})

def view(request, product_id):
    arch = get_object_or_404(Main, pk=product_id)
    return render(request, 'view.html', {'arch':arch})

def delete(request, id):
    delete_p = Main.objects.get(id=id)
    delete_p.delete()
    return redirect('home')

def edit(request, id):
    edit_post = Main.objects.get(id=id)
    return render(request, 'update.html', {'edit_post':edit_post})

def editrecord(request, id):
    name = request.POST['name']
    brand = request.POST['brand']
    price = request.POST['price']
    quanity = request.POST['quanity']
    
    malumot = Main.objects.get(id=id)
    malumot.name = name
    malumot.brand=brand
    malumot.price=price
    malumot.quanity=quanity
    malumot.save()
    return redirect('home')  