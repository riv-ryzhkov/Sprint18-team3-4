from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_rest_create'),
    path('detail/<int:pk>/', OrderDetailView.as_view()),
    path('all/', OrderListView.as_view()),
    path('', views.all_orders, name='orders'),
    path('<int:id>/', views.order_form, name='order'),
    path('<int:id>/delete/', views.order_delete, name='order_delete'),
    path('<int:id>/view/', views.order_by_id, name='order_by_id'),
]