from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    path('' , views.home , name = "home page"),
    path('about/' , views.about , name = "about_page"),
    path('contact/' , views.contact , name="contact"),
    path('register/', views.register , name="register"),
    path('api/posts/' , PostList.as_view() , name = "post_list" )
]