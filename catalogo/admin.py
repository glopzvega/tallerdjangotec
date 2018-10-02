from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class AdminModelBook(admin.ModelAdmin):
	list_display = ("title", "author", "publisher", "publisher_date", "pages", "language")