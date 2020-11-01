from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.utils import json


class TodoTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create(self):
        payload = {"title": "test title", "description": "test description"}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 1, "title": "test title", "description": "test description",
                                                "completed": False})

        payload = {"title": " ", "description": "demo description"}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"title": ["This field may not be blank."]})

        payload = {"title": "demo title", "description": " "}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"description": ['This field may not be blank.']})

        payload = {"title": "demo title", "description": "demo description "}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 2, "title": "demo title", "description": "demo description",
                                                "completed": False})

    def test_list(self):
        payload = {"title": "test title", "description": "test description"}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 1, "title": "test title", "description": "test description",
                                                "completed": False})

        payload = {"title": "demo title", "description": "demo description "}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 2, "title": "demo title", "description": "demo description",
                                                "completed": False})

        # list task
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, [{"id": 1, "title": "test title", "description": "test description",
                                                 "completed": False},
                                                {"id": 2, "title": "demo title", "description": "demo description",
                                                 "completed": False}])

    def test_update(self):
        payload = {"title": "test title", "description": "test description"}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 1, "title": "test title", "description": "test description",
                                                "completed": False})

        payload = {"title": "demo title", "description": "demo description "}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 2, "title": "demo title", "description": "demo description",
                                                "completed": False})

        response = self.client.get('/todo/2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 2, "title": "demo title", "description": "demo description",
                                                "completed": False})

        response = self.client.get('/todo/5')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"detail": "Not found."})

        # update task
        payload = {"completed": True}
        response = self.client.patch('/todo/2', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 2, "title": "demo title", "description": "demo description",
                                                "completed": True})

        payload = {"title": "title"}
        response = self.client.patch('/todo/1', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 1, "title": "title", "description": "test description",
                                                "completed": False})

    def test_delete(self):
        payload = {"title": "test title", "description": "test description"}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 1, "title": "test title", "description": "test description",
                                                "completed": False})

        payload = {"title": "demo title", "description": "demo description "}
        response = self.client.post('/todo/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"id": 2, "title": "demo title", "description": "demo description",
                                                "completed": False})
        # delete task
        response = self.client.delete('/todo/2')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/todo/2')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"detail": "Not found."})


