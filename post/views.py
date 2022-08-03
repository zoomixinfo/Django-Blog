from django.shortcuts import render
from . models import Post
from . forms import MakePost

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
def make(request):
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'make.html',{'form':MakePost()})
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return index(request)
def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = MakePost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'edit.html',{'form':MakePost(instance=post)})