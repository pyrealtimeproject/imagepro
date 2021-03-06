from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .forms import PostForm # new
from django.contrib.auth.forms import UserCreationForm


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

