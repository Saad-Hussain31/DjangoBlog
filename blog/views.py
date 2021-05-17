from django.shortcuts import render
# from django.http import HttpResponse (got rid of this import coz I
# am no longer returning HttpsResponse, but render template 
from .models import Post #why .? watch video 5 28:00
#pretend that we made a database call and got back this 'posts' list
#We wanna display this post on bloghome

# logic to handle different routes goes in this function
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
#fucntion to make about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

