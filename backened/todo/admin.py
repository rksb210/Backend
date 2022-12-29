from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','title','memo', 'created','completed','user']

# Register your models here.
