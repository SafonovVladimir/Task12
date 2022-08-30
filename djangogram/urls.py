from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsView.as_view(), name='home'),
    path('profile/', profile, name='users_profile'),
    # path('profile/<slug:user>/', profile, name='users_profile'),
    # path('profile/<user_name>/', PostsView.as_view(), name='user'),
    # path('', ViewPosts.as_view(), name='home'),
]
