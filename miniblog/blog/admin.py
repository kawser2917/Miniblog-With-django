from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(blogPost)
class blogPostAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
