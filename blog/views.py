from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.all() # taking all posts
    return render(request, 'index.html', {'posts':posts}) # Retornando o post no template

def post(request, post_id):
    posts = Post.objects.get(pk=post_id) # getting the specific post
    return render(request, 'post.html', {'posts':posts})