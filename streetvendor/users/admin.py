from django.contrib import admin
from .models import User

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password') # add fields as you want

admin.site.register(User, CustomUserAdmin)