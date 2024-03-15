from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)


# CRUD 

# Create
# Read -> List/Detail
# Update
# Delte
@login_required
def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')

@login_required
def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

@login_required
def create_service(request):
    if request.method == "POST":
        name = request.POST['title']
        body = request.POST['body']
        icon = request.POST['file']
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon,
        )
    return render(request, 'dashboard/service/create.html')

@login_required
def list_service(request):
    services = models.Service.objects.all()
    context = {
       'services':services
    }
    return render(request, 'dashboard/service/list.html', context)

@login_required
def create_aboutus(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body,
        )
    return render(request, 'dashboard/aboutus/create.html')

@login_required
def list_aboutus(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/list.html', context)

@login_required
def create_price(request):
    if request.method == "POST":
        title = request.POST['title']
        price = request.POST['price']
        body = request.POST['body']
        models.Price.objects.create(
            title=title,
            price=price,
            body=body,
        )
    return render(request, 'dashboard/price/create.html')


@login_required
def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/list.html', context)


@login_required
def banner_detail(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)

@login_required
def banner_edit(request, id):
    banner = models.Banner.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST['title']
        banner.body = request.POST['body']
        banner.save()
        return redirect('banner_detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)

@login_required
def banner_delete(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('list_banner')


# edit, detail, delete

@login_required
def  aboutus_detail(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/detail.html', context)


@login_required
def aboutus_edit(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
        aboutus.body = request.POST['body']
        aboutus.save()
        return redirect('aboutus_detail', aboutus.id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/edit.html', context)


@login_required
def aboutus_delete(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('list_aboutus')

@login_required
def price_detail(request, id):
    price = models.Price.objects.get(id=id)
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/detail.html', context)

@login_required
def price_edit(request, id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        price.title = request.POST['title']
        price.price = request.POST['price']
        price.body = request.POST['body']
        price.save()
        return redirect('price_detail', price.id)
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/edit.html', context)

@login_required
def price_delete(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('list_price')

@login_required
def service_detail(request, id):
    service = models.Service.objects.get(id=id)
    context = {
      'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)

@login_required
def service_edit(request, id): 
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST['title']
        service.body = request.POST['body']
        service.icon = request.POST['file']
        service.save()
        return redirect('service_detail', service.id)
    context = {
      'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)

@login_required
def service_delete(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('list_service')

@login_required
def contact_detail(request, id):
    contact = models.Contact.objects.get(id=id)
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/detail.html', context)

@login_required
def contact_edit(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.body = request.POST['body']
        contact.is_show = request.POST['is_show']
        contact.created_at = request.POST['created_at']
        contact.save()
        return redirect('contact_detail', contact.id)
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/edit.html', context)

@login_required
def contact_list(request):
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/list.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            User.objects.create_user(
                username = username,
                password = password
            )
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = User.objects.get(username=username)
        user = authenticate(
            username = username, 
            password = password
            )
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            ...

    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')

