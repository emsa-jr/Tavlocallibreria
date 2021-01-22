from django.contrib import admin
from catalogo.models import Author,Genre,Book.BookInstance
# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
