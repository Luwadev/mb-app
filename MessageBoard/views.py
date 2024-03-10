from django.shortcuts import render
from django.views.generic import ListView
from .models import MessageBoard

class HomePageView(ListView):
    model = MessageBoard
    template_name = 'home.html'
    context_object_name  = 'all_posts_list'

# Create your views here.
