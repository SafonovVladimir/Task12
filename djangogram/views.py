from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserLoginForm, UserRegisterForm, AddPostForm
from .models import *


def index(request):
    posts = Post.objects.all().order_by('-updated_at')
    user = request.user

    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, "djangogram/index.html", context=context)


@login_required
def profile(request, username):
    if username == str(request.user):
        user = request.user
        user_id = user.id
        profile = Profile.objects.get(user=user_id)
        posts = Post.objects.filter(author=user)
        images = Image.objects.filter(post__author=user)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'images': images,
        }
        return render(request, 'djangogram/profile.html', context)


def view_post(request, post_id):
    # post_item = Post.objects.get(pk=post_id)
    post_item = get_object_or_404(Post, pk=post_id)
    image = Image.objects.filter(post_id=post_id)
    context = {
        'item': post_item,
        'image': image,
    }
    return render(request, template_name='djangogram/view_post.html', context=context)


# class PostsView(ListView):
#     '''Список постів'''
#     model = Post
#     template_name = 'djangogram/index.html'
#     context_object_name = 'posts'

# def get_post(self, request):
#     posts = Post.objects.all()
#     image = Image.objects.all()
#     return render(request, "djangogram/index.html", {"posts": posts,
#                                                      "image": image})


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(pk=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('home')


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, "djangogram/index.html", {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'djangogram/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success')
            return redirect('home')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'djangogram/register.html', {'form': form})
