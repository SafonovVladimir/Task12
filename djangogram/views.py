from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag
from django.http import JsonResponse

from .forms import UserLoginForm, UserRegisterForm, AddPostForm, AddImageForm, UpdateUserProfile
from .models import *


def index(request):
    posts = Post.objects.all().select_related('author')
    profiles = Profile.objects.all().select_related('user')
    images = Image.objects.all().select_related('post')
    users = User.objects.filter().order_by('-date_joined')
    user = request.user
    context = {
        'posts': posts,
        'user': user,
        'profiles': profiles,
        'images': images,
        'users': users,
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
    user = User.objects.get(username=username)
    user_id = user.id
    profile = Profile.objects.get(user=user_id)

    following = Profile.objects.filter(followers=user_id)
    number_of_following = len(following)

    followers = profile.followers.all()
    if len(followers) == 0:
        is_following = False

    for follower in followers:
        if follower == request.user:
            is_following = True
            break
        else:
            is_following = False

    number_of_followers = len(followers)
    posts = Post.objects.filter(author=user)
    images = Image.objects.filter(post__author=user)
    count_posts = range(0, posts.count(), 3)
    context = {
        'user': user,
        'profile': profile,
        'posts': posts,
        'images': images,
        'count_posts': count_posts,
        'number_of_followers': number_of_followers,
        'number_of_following': number_of_following,
        'is_following': is_following,
    }
    return render(request, 'djangogram/profile.html', context)


def edit_profile(request, username):
    if request.method == 'POST':
        form = UpdateUserProfile(request.POST, request.FILES, instance=request.user.profile)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('user_profile', username)
        else:
            messages.error(request, 'Error')
    else:
        form = UpdateUserProfile(instance=request.user.profile)
        context = {
            'form': form,
            # 'profile': profile,
        }
    return render(request, 'djangogram/edit_profile.html', context=context)


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
            # Profile.objects.create(user=form.instance)
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


def add_followers(request, username):
    user_id = User.objects.get(username=username)
    profile = Profile.objects.get(user=user_id)
    profile.followers.add(request.user)
    return redirect('user_profile', username)


def remove_followers(request, username):
    user_id = User.objects.get(username=username)
    profile = Profile.objects.get(user=user_id)
    profile.followers.remove(request.user)
    return redirect('user_profile', username)


def view_followers(request, username):
    user_id = User.objects.get(username=username).id
    followers = Profile.objects.get(user=user_id).followers.all()
    context = {
        'followers': followers,
    }
    return render(request, "djangogram/followers.html", context=context)


def view_following(request, username):
    user_id = User.objects.get(username=username).id
    following = Profile.objects.filter(followers=user_id)
    context = {
        'following': following,
    }
    return render(request, "djangogram/following.html", context=context)


def validate_username(request):
    """Check available name"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

def check_username(request):
    """Check name"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

