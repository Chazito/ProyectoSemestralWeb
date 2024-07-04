from django.urls import path
from . import views

urlpatterns = [
    #path('index', views.index, name='index'),
    path('registro',views.registro, name = 'registro'),
    path('login',views.loginPage, name = 'login'),
    path('home',views.home, name= 'home'),
    path('profile/<str:username>',views.profile, name= 'home'),
    path('profile_edit',views.profile_edit, name= 'home'),
    path('forums',views.forum, name= 'home'),
    path('forums/<str:category>/',views.forum_cat, name= 'home'),
    path('post/<str:post_title>',views.post, name= 'home'),
    path('post/create',views.create_post, name= 'home'),
    path('cart',views.shopping_cart, name= 'home'),
    path('shop',views.shop, name= 'home'),
    path('membership',views.membership, name= 'home'),
    path('foros/', views.category_post, name='category_post'),
]