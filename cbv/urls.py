from django.urls import path
from .views import HomeView , AboutView , PostListView

urlpatterns = [
    path('', HomeView.as_view() , name = 'home'),
    path('about/' , AboutView.as_view() , name = 'about'),
    path('post/' , PostListView.as_view() , name = 'post-list'),
]