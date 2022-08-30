from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import UserLoginForm, UserRegisterForm, AddPostForm
from .models import *


@login_required
def profile(request):
    return render(request, 'djangogram/profile.html')


def index(request):
    post = Post.objects.all()
    context = {
        'posts': post,
        'title': 'Posts',
    }
    return render(request, template_name='djangogram/index.html', context=context)


class PostsView(ListView):
    '''Список постів'''
    model = Post
    template_name = 'djangogram/index.html'
    context_object_name = 'posts'

    # def get_post(self, request):
    #     posts = Post.objects.all()
    #     image = Image.objects.all()
    #     return render(request, "djangogram/index.html", {"posts": posts,
    #                                                      "image": image})


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
