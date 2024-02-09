import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from user.models import TwitterUser


# Create your tests here.
@pytest.mark.django_db
class TestTweetEndPoint:
    def test_that_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/tweets/', {'text': 'b'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_authorized_returns_201(self):
        client = APIClient()
        twitter_user = TwitterUser.objects.create(username='test_user', password='test_password')
        token = client.force_authenticate(user=twitter_user)
        client.credentials(HTTP_AUTHORIZATION=f'JWT {token}')
        response = client.post('/tweets/', {'text': 'b'})
        assert response.status_code == status.HTTP_201_CREATED

        # user = User.objects.create(username='test_user', password='test_password')
        # token = client.force_login(user=user)
        # client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        # response = client.post('/tweets/', {'text': 'b'})
        # assert response.status_code == status.HTTP_201_CREATED
