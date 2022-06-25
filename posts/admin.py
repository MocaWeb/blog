from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post
from . import models
# Register your models here.

@admin.register(models.Post)
class AuthorAdmin(SummernoteModelAdmin):
    list_display = ('author', 'title', 'slug',)
    prepopulated_fields = {'slug': ('title',), }

    summernote_fields = ('content',)

admin.site.register(Category)