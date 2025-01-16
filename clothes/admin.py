from django.contrib import admin
from .models import Garment, CustomUser

@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):
    list_display = ('cloth_type', 'size', 'price', 'publisher', 'created_at')
    list_filter = ('cloth_type', 'size', 'price', 'created_at')
    search_fields = ('description', 'publisher__full_name', 'type')
    ordering = ('-created_at',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'address')
    search_fields = ('username', 'full_name', 'email')
    ordering = ('username',)