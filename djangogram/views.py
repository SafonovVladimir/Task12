from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
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
