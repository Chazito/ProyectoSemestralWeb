from django.shortcuts import render
from .forms import CustomUserForm
from .models import Categoria

# Create your views here.
def index(request):
    form = CustomUserForm()
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'news/index.html',context)

def category_post(request):
    categorias = Categoria.objects.all()
    return render(request, 'category_post.html', {'categorias': categorias})