from django.contrib import admin
from book.models import Book
from author.models import Author
from authentication.models import CustomUser
from order.models import Order


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(CustomUser)
admin.site.register(Order)