from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    form = CustomUserForm()
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'news/index.html',context)

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