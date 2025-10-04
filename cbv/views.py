from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post


# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Class based view concept!")
    

class AboutView(View):
    def get(self , request):
        return render(request, 'cbv/about.html')
    

class PostListView(ListView):
    model = Post
    template_name = 'cbv/post_list.html'
    context_object_name = 'posts'

