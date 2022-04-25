from django.shortcuts import render, redirect

# Create your views here.
from .models import BlogPost
from .form   import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def check_post_owner(blogpost, request):
    """Make sure blogpost owner matchs the curren request user"""
    if blogpost.owner != request.user:
        raise Http404

def index(request):
    """Homepage"""
    posts = BlogPost.objects.order_by('-date_added')
#    for post in posts:
#        head = post.title
#        body = post.text 
#        date = post.date_added
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        #No data submitted. create a blank form.
        form = BlogPostForm()
    else:
        #POST data submitted;process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            """
            #Slove IntegrityError at /new_post/
NOT NULL constraint failed: blogs_blogpost.owner_id
Exception Value:
NOT NULL constraint failed: blogs_blogpost.owner_id
"""
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')


    context = {'form':form}    
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    check_post_owner(post, request)
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
