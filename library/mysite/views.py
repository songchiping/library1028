from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from .filters import Search

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html' , locals())

def showpost(request, slug):
    post = Post.objects.get(slug=slug) 
    return render(request, 'post.html', locals())
    
def show_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'allposts.html', locals())

def show_comments(request, post_id):
    comments = Post.objects.get(id=post_id).comment_set.all()
    return render(request, 'comments.html', locals())

def index(request):
    post = Post.objects.all()
    if request.method == "POST":
        search = Search(request.POST, queryset=post)
    else:
        search = Search(request.GET, queryset=post)
    context = {'search': search}
    return render(request, 'index2.html', context)

