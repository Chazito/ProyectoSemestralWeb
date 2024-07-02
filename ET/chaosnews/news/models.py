from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_title = models.CharField(max_length=50)

class NewsPost(models.Model):
    post_id = models.IntegerField(primary_key=True)
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
    