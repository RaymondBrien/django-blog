from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # automatically assigns as post_list - accessible for templates logic 
    # given the Model name and the type of view: here as Post and Listview. 
    template_name = "blog/index.html" 
    paginate_by = 6
    
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1) # only published posts
    post = get_object_or_404(queryset, slug=slug) # matching specific slug only, otherwise 404 error

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        },

    )