from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import Categoria
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def category_post(request):
    categorias = Categoria.objects.all()
    return render(request, 'category_post.html', {'categorias': categorias})

def registro(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
        else:
            messages.error(request, form.errors.as_text())
    else:
        form = CustomUserForm()
    
    context = {'form':form}
    return render(request, 'news/registro.html',context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nombre o contraseña incorrecta.')
    context = {}
    return render(request, 'news/login.html',context)

def home(request):
    context = {}
    return render(request, 'news/home.html', context)

def profile(request, username):
    context = {'username':username}
    return render(request, 'news/profile.html', context)

def forum(request):
    context = {}
    return render(request, 'news/forum.html', context)

def forum_cat(request, category):
    context = {'category':category}
    return render(request, 'news/forum_cat.html', context)

def post(request):
    context = {}
    return render(request, 'news/post.html', context)

def profile_edit(request, username):
    context = {'username':username}
    return render(request, 'news/profile_edit.html', context)

def shop(request):
    context = {}
    return render(request, 'news/shop.html', context)

def membership(request):
    context = {}
    return render(request, 'news/membership.html', context)

def shopping_cart(request):
    context = {}
    return render(request, 'news/cart.html', context)

def create_post(request):
    context = {}
    return render(request, 'news/create_post.html', context)
