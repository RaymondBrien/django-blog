from django.shortcuts import render
from django.views import generic 
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # automatically expects a template called post_list 
    # given the Model name and the type of view: here as Post and Listview. 
    # Should not change file name in workspace but can use template_name
    # to give it a custom name if we want 
    template_name = "post_list.html" 