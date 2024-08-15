from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Home Page")
# Create your views here.


def about_page_view(request):
    context = {
        "name":"Debo",
        "age": "35"
        }
    return render(request,"pages/about.html", context)