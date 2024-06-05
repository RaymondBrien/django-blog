from django.shortcuts import render
from django.views import generic 
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # automatically assigns as post_list - accessible for templates logic 
    # given the Model name and the type of view: here as Post and Listview. 
    template_name = "blog/index.html" 
    paginate_by = 6