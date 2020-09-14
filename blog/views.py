from django.shortcuts import render
from django.view.generic import ListView
from .models import Posts

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html"