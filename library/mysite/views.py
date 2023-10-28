from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html' , locals())

def showpost(request, slug):
    try:
        post=Post.objects.get(slug=slug)
        if post != None:            
            return render(request, 'post.html' , locals())
        else:
            return redirect("/") #導到首頁
    except:
        return redirect("/")

# def homepage(request):    
#     post = Post.objects.all() #select * from post
#     post_lists = list()
#     for counter,post in enumerate(post):
#         post_lists.append(f'No.{counter}{post}<br>')
#     return HttpResponse(post_lists)

# def showpost(request, slug):
#     post = Post.objects.get(slug=slug)
#     return render(request ,'post.html', locals())