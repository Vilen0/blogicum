from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Используем кастомную форму для добавления
    model = MyUser
    list_display = ['username', 'bio', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'bio']
    ordering = ['username']

admin.site.register(MyUser, CustomUserAdmin)
