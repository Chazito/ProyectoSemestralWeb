from django.shortcuts import render, redirect
from .forms import CustomUserForm
<<<<<<< HEAD
from .models import Categoria
=======
from django.contrib import messages
>>>>>>> 747fa1c40d58f328c5b0f4c71970312106e7bab8

# Create your views here.
def index(request):
    form = CustomUserForm()
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'news/index.html',context)

<<<<<<< HEAD
def category_post(request):
    categorias = Categoria.objects.all()
    return render(request, 'category_post.html', {'categorias': categorias})
=======
def registro(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
        else:
            messages.error(request, '')
    else:
        form = CustomUserForm()
    
    context = {'form':form}
    return render(request, 'news/registro.html',context)
>>>>>>> 747fa1c40d58f328c5b0f4c71970312106e7bab8
