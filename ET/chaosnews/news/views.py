from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserForm, NewsPostForm
from .models import NewsCategory, UserProfile, NewsPost
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def category_post(request):
  categorias = NewsCategory.objects.all().order_by('category_title')
  context = {'categorias':categorias}
  return render(request, 'news/category_post.html', context)


def registro(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(username = user)
            profile.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
        else:
            messages.error(request, form.errors.as_text())
    else:
        form = CustomUserForm()
    
    context = {'form':form}
    return render(request, 'news/registro.html',context)

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
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

# Hay que hacer que esté logeado para crear post? 
def create_post(request):
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)  # Redirige a la vista de detalle del post
    else:
        form = NewsPostForm()
    return render(request, 'news/create_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})

def post_list(request):
    user_posts = NewsPost.objects.filter(post_author=request.user)
    return render(request, 'news/post_list.html', {'user_posts': user_posts})

def category_posts(request, category_id):
    category = get_object_or_404(NewsCategory, id_cat=category_id)
    posts = NewsPost.objects.filter(post_category=category)
    return render(request, 'news/category_posts.html', {'category': category, 'posts': posts})

def user_posts(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    posts = NewsPost.objects.filter(post_author=user)
    return render(request, 'news/user_posts.html', {'user': user, 'posts': posts})
