from django.urls import path

from .views import *

urlpatterns = [
    path('', post_view, name='home'),
    path('like/', like_post, name='like_post'),
    path('profile/', profile, name='users_profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_post/', add_post, name='add_post'),
    path('register/', register, name='register'),
]
