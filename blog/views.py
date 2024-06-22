from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on") # from newest to oldest
    comment_count = post.comments.filter(approved=True).count() # .comments for comments and comment_count variables: accessible from Comments model via related name

    if request.method == "POST":
        print("Received POST")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm() # resets content of form to blank to enable user to write another comment

    print("About to render template")
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },

    )