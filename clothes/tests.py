from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Garment

class ClothesMarketplaceTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

        self.garment = Garment.objects.create(
            cloth_type='shirt', 
            description='Test Shirt', 
            size='M', 
            price=20.0,
            publisher=self.user
        )

    def test_publish_garment(self):
        """Test publishing a new garment."""
        url = '/clothes/publish/' 
        data = {
            'cloth_type': 'pants',
            'description': 'Test Pants',
            'size': 'L',
            'price': 25.0,
        }
        headers = {
            'Authorization': f'Bearer {self.access_token}'  
        }
        response = self.client.post(url, data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unpublish_garment(self):
        """Test unpublishing a garment."""
        url = f'/clothes/{self.garment.id}/unpublish/'  
        headers = {
            'Authorization': f'Bearer {self.access_token}' 
        }
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unpublish_garment_by_other_user(self):
        """Test that another user cannot unpublish a garment."""
        another_user = get_user_model().objects.create_user(username='anotheruser', password='password')
        
        refresh = RefreshToken.for_user(another_user)
        access_token = str(refresh.access_token)

        url = f'/clothes/{self.garment.id}/unpublish/'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = self.client.delete(url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_garment(self):
        """Test updating a garment."""
        url = f'/clothes/{self.garment.id}/update/' 
        data = {
            'cloth_type': 'jacket',
            'description': 'Updated Jacket',
            'size': 'L',
            'price': 30.0,
        }
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        response = self.client.put(url, data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unpublish_garment_by_other_user(self):
        """Test that another user cannot update a garment."""
        another_user = get_user_model().objects.create_user(username='anotheruser', password='password')

        refresh = RefreshToken.for_user(another_user)
        access_token = str(refresh.access_token)

        url = f'/clothes/{self.garment.id}/unpublish/'
        data = {
            'cloth_type': 'jacket',
            'description': 'Updated by another user',
            'size': 'L',
            'price': 30.0,
        }
        headers = {
            'Authorization': f'Bearer {access_token}' 
        }
        response = self.client.delete(url, data, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
