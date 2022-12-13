from django.contrib import admin
from django.urls import path
from engine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit/<int:id>/', views.edit_new, name='edit'),
    path('delete/<int:id>/', views.delete_new, name='delete'),
    path('add/', views.add_new, name='add'),
    path('all/', views.all_posts, name='all'),
]
