from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('like/', like_post, name='like_post'),
    path('profile/<slug:username>', profile, name='user_profile'),
    path('profile/edit/<slug:username>', edit_profile, name='edit_profile'),
    path('user/<slug:author>', get_user_posts, name='user_posts'),
    path('tags/<slug:tag>', get_tag_posts, name='tag_posts'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_post/', add_post, name='add_post'),
    path('register/', register, name='register'),
    path('post/<int:post_id>', view_post, name='view_post'),
]
