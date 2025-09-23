from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_posts", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")    
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = CKEditor5Field(blank=True, null=True)
    # body = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User,related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()




    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        return reverse("home")
        # return reverse("article_detail", args=(str(self.id)))





class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(null=True,blank=True,upload_to="images/profile/",default="images/profile/default.png" )
    linkedin_url = models.CharField(max_length=255,null= True,blank=True)
    insta_url = models.CharField(max_length=255,null= True,blank=True)
    github_url = models.CharField(max_length=255,null= True,blank=True)
    # social_media = models.CharField(max_length=255,null= True,blank=True)


    def __str__(self):
        return str(self.user)
    


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "%s - %s"  % (self.post.title,self.name)    