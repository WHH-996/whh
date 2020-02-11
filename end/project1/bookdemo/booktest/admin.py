from django.contrib import admin

# Register your models here.

# Django自带的后台管理操作需要在此实现

from .models import Book, Hero
admin.site.register(Book)
admin.site.register(Hero)