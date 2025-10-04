from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, RegisterForm
from django.contrib.auth import authenticate , login , logout 


# def home(request):
#     return HttpResponse("The blog app is running.")

def home(request):
    return render(request ,'blog/home.html')


def about(request):
    return HttpResponse("<h1>This is the about page of blog app.<h1>")

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        return render(request,'blog/success.html',{'name':name})
    return render(request,'blog/contact.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password = password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request , 'blog/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)
    

    def post(self , request):
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)