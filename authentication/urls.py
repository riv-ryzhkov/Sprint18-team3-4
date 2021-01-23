from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name='user_rest_create'),
    path('detail/<int:pk>/', CustomUserDetailView.as_view()),
    path('all/', CustomUserListView.as_view()),
    path('', views.all_users, name='users'),
    path('<int:id>/', views.user_form, name='user'),
    path('<int:id>/view', views.user_by_id, name='user_by_id'),
    path('<int:id>/delete/', views.user_delete, name='user_delete'),
]
