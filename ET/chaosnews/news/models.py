from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsCategory(models.Model):
    id_cat = models.AutoField(primary_key=True, db_column='idCategoria')
    category_title = models.CharField(max_length=50, blank=False, null=False)

class NewsPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_story = models.CharField(max_length=2000)
    post_date = models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Moneda(models.Model):
    package_name = models.CharField(max_length=200, blank=False, null=False)
    price = models.IntegerField()
    ammount = models.IntegerField()

class ShoppingCart(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    
class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
