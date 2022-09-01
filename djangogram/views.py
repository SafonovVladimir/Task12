from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserLoginForm, UserRegisterForm, AddPostForm, AddImageForm
from .models import *


def index(request):
    posts = Post.objects.all().order_by('-updated_at')
    profiles = Profile.objects.all()
    user = request.user
    context = {
        'posts': posts,
        'user': user,
        'profiles': profiles,
    }
    return render(request, "djangogram/index.html", context=context)


def get_user_posts(request, author):
    user_id = User.objects.get(username=author).id
    posts = Post.objects.filter(author=user_id).order_by('-updated_at')

    context = {
        'posts': posts,
    }
    return render(request, "djangogram/index.html", context=context)


def get_tag_posts(request, tag):
    tag_id = Tag.objects.get(url=tag).id
    posts = Post.objects.filter(tags=tag_id).order_by('-updated_at')
    profiles = Profile.objects.all()
    context = {
        'posts': posts,
        'profiles': profiles
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
    profiles = Profile.objects.all()
    context = {
        'post': post_item,
        'image': image,
        'profiles': profiles,
    }
    return render(request, template_name='djangogram/view_post.html', context=context)


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
        post = AddPostForm(request.POST, request.FILES, prefix='post')
        image = AddImageForm(request.POST, request.FILES, prefix='image')
        context = {
            'post': post,
            'image': image
        }
        if post.is_valid() and image.is_valid():
            p = post.save()
            image.cleaned_data['post'] = p
            image.save()
            messages.success(request, 'Success')
            return redirect('home')
    else:
        post = AddPostForm(prefix='post')
        image = AddImageForm(prefix='image')
        context = {
            'post': post,
            'image': image
        }
    return render(request, "djangogram/add_post.html", context=context)


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
