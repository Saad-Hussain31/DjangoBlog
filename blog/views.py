from django.shortcuts import render
from django.http import HttpResponse



# logic to handle different routes goes in this function
def home(request):
    return HttpResponse('<h1> Blog Home </h1>')

#fucntion to make about page
def about(request):
    return HttpResponse("<h1>Blog About </h1>")