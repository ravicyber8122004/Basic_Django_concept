from django.shortcuts import render

# Create your views here.
# def  home(request):
#     return render(request , 'shop/home.html' , {'name':''})

def home(request):
    return render(request ,'shop/home.html', {'user':''} )