
from django.shortcuts import render, get_object_or_404

from .models import Post

# this is what will handle the request
def post_list(request):

    posts = Post.objects.all();
    # breakpoint()
    # note the following will render the template created.
    return render(request, 'blog/posts_list.html', {'posts': posts})

def post_detail(request, pk):
    # get the post with the given primary key (pk) from the database
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})