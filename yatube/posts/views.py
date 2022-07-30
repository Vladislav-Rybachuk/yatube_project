from django.shortcuts import render
from django.http import HttpResponse


# General page
def index(request):
    template = 'posts/index.html'
    return render(request, template)

# Page with  filtered posts
def group_posts(request,slug):
    group_template ='group_list.html'
    return render(request,group_template)
