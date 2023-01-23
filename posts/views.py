from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    template_name = 'posts/list.html'
    queryset = Post.objects.all()
    context_object_name ='posts'
    
    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
