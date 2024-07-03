from django.urls import path
from . import views

urlpatterns = [
    #path('index', views.index, name='index'),
    path('index',views.index, name = 'index'),
    path('foros/', views.category_post, name='category_post'),
]