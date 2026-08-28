from django.http import HttpResponse
from django.shortcuts import render
def home(request):
   # return HttpResponse("Hello, world. This is my Django Home page")
   return render(request,'website/index.html')
def about(request):
    return HttpResponse("Hello, world. This is my Django About page")

def contact(request):
    return HttpResponse("Hello, world. This is my Django contact page")
