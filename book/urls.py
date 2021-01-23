from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('create/', BookCreateView.as_view(), name='book_rest_create'),
    path('detail/<int:pk>/', BookDetailView.as_view()),
    path('all/', BookListView.as_view()),
    path('test/', views.test, name='test'),
    path('<int:id>/', views.book_form, name='book'),
    path('<int:id>/view', views.book_by_id, name='book_by_id'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),
]