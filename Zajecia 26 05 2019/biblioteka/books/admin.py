from django.contrib import admin
from books.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','cover_type']
    search_fields = ['title']


admin.site.register(Book,BookAdmin)

