from django.shortcuts import render
# from django.http import HttpResponse (got rid of this import coz I
# am no longer returning HttpsResponse, but render template 

#pretend that we made a database call and got back this 'posts' list
#We wanna display this post on bloghome
posts = [
   {
        'author': 'Saad Hussain',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2021'    
   },
   {
        'author': 'Tolstoy',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2021'    
   }

]

# logic to handle different routes goes in this function
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)
#fucntion to make about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

