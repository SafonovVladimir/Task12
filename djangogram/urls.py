from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsView.as_view(), name='home'),
    path('profile/', profile, name='users_profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_post/', add_post, name='add_post'),
    path('register/', register, name='register'),
]
