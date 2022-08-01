from django.shortcuts import render
from . models import Post

def index(request):
    post = {
        'post':Post.objects.all()
    }
    return render(request, 'index.html',post)
def post(request, id):
    post = {
        'post':Post.objects.get(id=id)
    }
    return render(request, 'post.html',post)