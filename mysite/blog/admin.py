from django.contrib import admin
from .models import Post # import Post class from model file in blog app

admin.site.register(Post)
# Register your models here.
