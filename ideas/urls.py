from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('idea/new/', views.ideaCreate, name='idea-create'),
    path('ideas/', views.ideaList, name='idea-list'),
    path('idea/<int:pk>/', views.ideaUpdate, name='idea-update'),
    path('idea/<int:pk>/delete', views.ideaDelete, name='idea-delete'),
    path('tag/<int:pk>/', views.tagHome, name='tag-home'),
]
