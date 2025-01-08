from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
@login_required(login_url='/users/login/')
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required(login_url='/users/login/')
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
                newpost = form.save(commit=False)
                newpost.author = request.user
                newpost.save()
                return redirect('posts:list')
    else:
        form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form})

@login_required(login_url='/users/login/')
def edit_post(request, slug):
    post = Post.objects.get(slug=slug)

    if post.author != request.user:
        return redirect('posts:list')
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})
         
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("posts:list")
    return render(request, 'posts/delete_post.html', {'post': post})