'''
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import User
from Library import settings

class UserTests(APITestCase):
    def should_successfully_create_user(self):
        url = reverse('user')
        data = {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@user.com',
            'username': 'user',
            'password': '123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def should_successfully_delete_user(self):
        url = reverse('user/2')
        data = {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@user.com',
            'username': 'user',
            'password': '123'
        }
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class AuthorTests(APITestCase):
    def should_successfully_create_author(self):
        url = reverse('author')
        data = {'name': 'George Orwell'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def should_successfully_delete_author(self):
        url = reverse('author/4')
        data = {'name': 'George Orwell'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def should_return_character_limit_error(self):
        url = reversed('author')
        data = {'name': '12345678901234567890123456789012345678901234567890123456789012345678901234567890123'
                        '4567890123456789044'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def should_return_required_field_error(self):
        url = reversed('author')
        data = {'name': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
'''

'''
from django.test import TestCase
from django.urls import reverse, resolve
from app.views import UserViewSet


class UserTestCase(TestCase):
    def test_resolver_list_url(self):
        _resolve = self.resolve_by_name('user')
        self.assertEqual(_resolve.func.cls, UserViewSet)
'''
