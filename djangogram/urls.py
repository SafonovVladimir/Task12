from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('like/', like_post, name='like_post'),
    path('profile/<slug:username>', profile, name='user_profile'),
    path('profile/<slug:username>/followers/add', add_followers, name='add_follower'),
    path('profile/<slug:username>/followers/remove', remove_followers, name='remove_follower'),
    path('profile/edit/<slug:username>', edit_profile, name='edit_profile'),
    path('user/<slug:author>', get_user_posts, name='user_posts'),
    path('tags/<tag_slug>', get_tag_posts, name='tag_posts'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_post/', add_post, name='add_post'),
    path('register/', register, name='register'),
    path('post/<int:post_id>', view_post, name='view_post'),
    path('followers/<username>', view_followers, name='followers'),
    path('following/<username>', view_following, name='following'),
    path('validate_username/', validate_username, name='validate_username'),
    path('check_username/', check_username, name='check_username'),
]
