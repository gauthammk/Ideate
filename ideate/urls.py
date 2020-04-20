from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from ideas import views as idea_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.loginUser, name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', user_views.logoutUser, name='logout'),
    path('update/', user_views.update, name='update'),
    path('error/', idea_views.error, name='error'),
    path('', include('ideas.urls')),
]
