from django.test import SimpleTestCase
from django.urls import resolve, reverse
from djangogram.views import *


class TestUrls(SimpleTestCase):

    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_login_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, user_login)

    def test_logout_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, user_logout)

    def test_register_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_view_post_is_resolved(self):
        url = reverse('view_post', args=[2])
        self.assertEqual(resolve(url).func, view_post)

    def test_profile_is_resolved(self):
        url = reverse('user_profile', args=['admin'])
        self.assertEqual(resolve(url).func, profile)

    def test_edit_profile_is_resolved(self):
        url = reverse('edit_profile', args=['admin'])
        self.assertEqual(resolve(url).func, edit_profile)

    def test_user_post_is_resolved(self):
        url = reverse('user_posts', args=['admin'])
        self.assertEqual(resolve(url).func, get_user_posts)
