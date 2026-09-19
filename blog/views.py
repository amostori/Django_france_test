from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request): 
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully')
        return redirect('home')
    else:
        all_posts = Post.objects.all()
    
    return render(request, 'home.html', {'all_posts': all_posts})

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home')
