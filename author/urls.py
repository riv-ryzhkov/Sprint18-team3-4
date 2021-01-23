from . import views
from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)


urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='author_rest_create'),
    path('detail/<int:pk>/', AuthorDetailView.as_view()),
    path('all/', AuthorListView.as_view()),
    path('', views.all_authors, name='authors'),
    path('<int:id>/', views.author_form, name='author'),
    path('<int:id>/view', views.author_by_id, name='author_by_id'),
    path('<int:id>/delete/', views.author_delete, name='author_delete'),
]



# path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]
# urlpatterns = [