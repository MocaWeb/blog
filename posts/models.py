from cgitb import text
from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        # app_label = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:category", kwargs={"name": self.name})


class Post(models.Model):
    STATUS = (("DRAFT", "Draft"), ("PUBLISHED", "Published"))

    category = models.ManyToManyField(Category, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique_for_date="published_date")
    content = models.TextField() 
    published_date = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)
    status = models.CharField(default="DRAFT", choices=STATUS, max_length=10)

    # tags mechanism
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:details_post", kwargs={"slug": self.slug})


    def is_draft(self):
        return self.status == "DRAFT"
