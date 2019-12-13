from django.contrib import admin
from .models import Entries, Category, Post

# Register your models here.
admin.site.register(Entries)
admin.site.register(Category)
admin.site.register(Post)
