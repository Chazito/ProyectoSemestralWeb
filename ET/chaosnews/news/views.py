from django.shortcuts import render
from .forms import CustomUserForm

# Create your views here.
def index(request):
    form = CustomUserForm()
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'news/index.html',context)