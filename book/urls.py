from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('test/', views.test, name='test'),
    path('<int:id>/', views.book_form, name='book'),
    path('<int:id>/view', views.book_by_id, name='book_by_id'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),
]