from django.urls import path
from . import views

urlpatterns = [
    #path('index', views.index, name='index'),
    path('registro',views.registro, name = 'registro'),
    path('login',views.loginPage, name = 'login'),
    path('logout',views.cerrar_sesion, name = 'logout'),
    path('home',views.home, name= 'home'),
    path('profile/<str:username>',views.profile, name= 'profile'),
    path('profile_edit',views.profile_edit, name= 'profile_edit'),
    path('forums',views.category_post, name= 'forum'),
    path('forums/<str:category>/',views.forum_cat, name= 'forum_cat'),
    path('post/<str:post_title>',views.post, name= 'post'),
    path('post/create',views.create_post, name= 'create_post'),
    path('cart',views.shopping_cart, name= 'cart'),
    path('shop',views.shop, name= 'shop'),
    path('membership',views.membership, name= 'membership'),
    path('foros/', views.category_post, name='category_post'),
    path('finanzas/', views.category_post, name='finanzas_category'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('user/<int:user_id>/', views.user_posts, name='user_posts'),
]