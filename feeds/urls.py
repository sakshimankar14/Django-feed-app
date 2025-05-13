from django.urls import path
from . import views

app_name = 'feeds'  # Maintain this namespace for URL reversing

urlpatterns = [
    # Feed listing and creation
    path('', views.feed_list, name='feed_list'),
    
    # Feed deletion
    path('delete/<int:pk>/', views.delete_feed, name='delete_feed'),
    
    # Like functionality (add this new line)
    path('like/<int:pk>/', views.like_feed, name='like_feed'),
    
    # Future-proof additions (uncomment when needed):
    # path('create/', views.feed_create, name='feed_create'),
    # path('edit/<int:pk>/', views.feed_edit, name='feed_edit'),
    # path('detail/<int:pk>/', views.feed_detail, name='feed_detail'),
]