from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("about func")
def contact(request):
    return HttpResponse("contact func")
def tracker(request):
    return HttpResponse("tracker func")
def search(request):
    return HttpResponse("search func")
def productview(request):
    return HttpResponse("productview func")
def checkout(request):
    return HttpResponse("checkout func")
