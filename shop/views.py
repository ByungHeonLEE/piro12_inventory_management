from django.shortcuts import render, redirect
from django.urls import reverse
from shop.models import Product, Client
from .forms import ProductForm, ClientForm


def list_product(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'list_product.html', data)


def list_client(request):
    clients = Client.objects.all()
    data = {
        'clients': clients
    }
    return render(request, 'list_client.html', data)


def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'product': product
    }
    return render(request, 'detail_product.html', data)


def detail_client(request, pk):
    client = Client.objects.get(pk=pk)
    products = Product.objects.filter(client=client)
    data = {
        'client': client,
        'products': products
    }
    return render(request, 'detail_client.html', data)


def reg_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save()
            return redirect(reverse('detail_product', kwargs={'pk': product.pk}))
    else:
        form=ProductForm()
    return render(request, 'reg_product.html', {
        'form':form,
    })

def reg_client(request):
    if request.method =='POST':
        form=ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client=form.save()
            return redirect(reverse('detail_client', kwargs={'pk': client.pk}))
    else:
        form=ClientForm()
    return render(request, 'reg_client.html', {
        'form':form,
    })

def update_client(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method =='POST':
        form=ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            client=form.save()
            return redirect(reverse('detail_client', kwargs={'pk': client.pk}))
    else:
        form=ClientForm()
    return render(request, 'update_client.html', {
        'form':form,'client': client
    })

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            product.save()
            return redirect(reverse('detail_product', kwargs={'pk': product.pk}))
    else:
        form=ProductForm()
    return render(request, 'update_product.html', {
        'form':form, 'product': product
    })

def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('list_client')
    return redirect(reverse('delete_client', kwargs={'pk': client.pk}))


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_product')
    return redirect(reverse('delete_product', kwargs={'pk': product.pk}))


def minus_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.left -= 1
        product.save()
        return redirect('list_product')
    return redirect(reverse('minus_product', kwargs={'pk': product.pk}))
def plus_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.left += 1
        product.save()
        return redirect('list_product')
    return redirect(reverse('plus_product', kwargs={'pk': product.pk}))