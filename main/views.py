import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
import datetime
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username, # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def register_flutter(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False, "message": "Register gagal, username sudah digunakan."}, status=400)
    
        if username is not None and password is not None:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'status': True, 'message': 'Sukses membuat akun'}, status=201)
    return JsonResponse({'error': 'Invalid Method'}, status=400)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.user == request.user:
        item.delete()
        messages.success(request, 'Berhasil menghapus '+item.name)
    return HttpResponseRedirect(reverse('main:show_main'))

def tambah_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.user == request.user and item.amount > 0:
        item.amount += 1
        item.save()
        messages.success(request, 'Berhasil menambahkan '+item.name)
    else:
        messages.error(request, 'Gagal menambahkan '+item.name)
    return HttpResponseRedirect(reverse('main:show_main'))

def kurang_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.user == request.user:
        if item.amount == 1:
            delete_item(request, id)
        if item.amount > 1:
            item.amount -= 1
            item.save()
            messages.success(request, 'Berhasil mengurangi '+item.name)
    else:
        messages.error(request, 'Gagal mengurangi '+item.name)
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, user=user)
        new_product.save()

        response_data = {
            'success': True,
            'message': 'Berhasil menambahkan ' + name
        }
    return JsonResponse(response_data)

@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        item = Item.objects.get(pk=id)
        item.delete()

        response_data = {
            'success': True,
            'message': 'Berhasil menghapus ' + item.name
        }
    return JsonResponse(response_data)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    

