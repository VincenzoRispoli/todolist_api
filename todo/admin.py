from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'created_at', 'user']


admin.site.register(Todo, TodoAdmin)
