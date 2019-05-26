from django.contrib import admin
from authors.models import Author
# Register your models here.

@admin.register(Author)
class AuthorsAdmin(admin.ModelAdmin):
    pass