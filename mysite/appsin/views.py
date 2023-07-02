from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'appsin/index.html')

def about(request):
    return render(request, 'appsin/about.html')

def service(request):
    return render(request, 'appsin/service.html')

def contact(request):
    return render(request, 'appsin/contact.html')

def search(request):
    return render(request, 'appsin/search.html')
