from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

User = get_user_model()

class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="user",
            password="secret",
        )
        cls.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
        )

        cls.post = Post.objects.create(
            title='Sample Post',
            body='Sample Body',
            author=cls.user,
        )

        cls.post_list_url = reverse('posts-list')
        cls.post_detail_url = reverse('posts-detail', kwargs={'pk': 
                                cls.post.pk})


    def test_list_authenticated(self):
        self.client.login(username='user', password='secret')
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_detail_authenticated(self):
        self.client.login(username='user', password='secret')
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation_as_authenticated(self):
        self.client.login(username='user', password='secret')
        response = self.client.post(
            self.post_list_url,
            {'title': 'New Post', 'body': 'New Content', 'author': self.user.id}
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().author, self.user)

