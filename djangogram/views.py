from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag

from .forms import UserLoginForm, UserRegisterForm, AddPostForm, AddImageForm
from .models import *


def index(request):
    posts = Post.objects.all().select_related('author')
    profiles = Profile.objects.all().select_related('user')
    images = Image.objects.all().select_related('post')
    user = request.user
    context = {
        'posts': posts,
        'user': user,
        'profiles': profiles,
        'images': images,
    }
    return render(request, "djangogram/index.html", context=context)


def get_user_posts(request, author):
    user_id = User.objects.get(username=author).id
    posts = Post.objects.filter(author=user_id).order_by('-updated_at')
    profiles = Profile.objects.all()
    context = {
        'posts': posts,
        'profiles': profiles,
    }
    return render(request, "djangogram/index.html", context=context)


def get_tag_posts(request, tag_slug):
    post = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = post.filter(tags__in=[tag])

    profiles = Profile.objects.all()
    context = {
        'posts': posts,
        'profiles': profiles,
        'tag': tag,
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
        count_posts = range(0, posts.count(), 3)
        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'images': images,
            'count_posts': count_posts,
        }
        return render(request, 'djangogram/profile.html', context)


def edit_profile(request, username):
    # if username == str(request.user):
    #     user = request.user
    #     user_id = user.id
    #     profile = Profile.objects.get(user=user_id)
    #     posts = Post.objects.filter(author=user)
    #     images = Image.objects.filter(post__author=user)
    #
    #     context = {
    #         'user': user,
    #         'profile': profile,
    #         'posts': posts,
    #         'images': images,
    #     }
    return render(request, 'djangogram/edit_profile.html')  # , context)


def view_post(request, post_id):
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
    user = request.user
    if request.method == 'POST':
        post = AddPostForm(request.POST)
        images = request.FILES.getlist("image")
        context = {
            'post': post,
            'images': images,
        }
        if post.is_valid():
            instance = post.save(commit=False)
            instance.author = user
            instance.save()
            for image in images:
                Image.objects.create(post=instance, image=image)
            post.save_m2m()
            messages.success(request, 'Success')
            return redirect('home')
    else:
        post = AddPostForm()
        images = AddImageForm()
        context = {
            'post': post,
            'images': images,
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
        context = {
            'form': form,
        }
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=form.instance)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
        context = {
            'form': form,
        }
    return render(request, 'djangogram/register.html', context=context)
