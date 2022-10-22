from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse('<h2>Hello World</h2')