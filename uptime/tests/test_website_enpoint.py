from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from uptime.models import WebsiteEndpoint
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class WebsiteEndpointTestCase(APITestCase):
    """
    API Tests for WebsiteEndpoint
    """

    def setUp(self):
        self.detail_route = "websiteendpoint-detail"
        self.list_route = "websiteendpoint-list"
        self.model = WebsiteEndpoint
        self.user_sample = {"username": "website", "email": "website@culiops.xyz"}
        user = User.objects.create(
            username=self.user_sample["username"], email=self.user_sample["email"]
        )
        self.init_item = self.model.objects.create(
            account_id="000000",
            arn="000000",
            email="000000@culiops.xyz",
            joined_method="000000",
            joined_timestamp="2021-10-10 11:11:11.184106+00:00",
            name="test",
        )
        self.valid_payload = {
            "account_id": "111111",
            "arn": "111111",
            "email": "111111@culiops.xyz",
            "joined_method": "CREATED",
            "joined_timestamp": "2021-10-10 11:11:11.184106+00:00",
            "name": "test1",
        }
        self.invalid_payload = {
            "account_id": "111111",
            "arn": "111111",
            "email": "111111",
            "joined_method": "111111",
            "joined_timestamp": "111111",
            "name": "",
        }
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_valid_create(self):
        """
        Ensure we can create an new valid instance.
        """
        url = reverse(self.list_route)
        data = self.valid_payload
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.model.objects.count(), 2)
        self.assertEqual(response.data["name"], self.valid_payload["name"])

    def test_invalid_create(self):
        """
        Ensure we can not create an new instance with invalid payload.
        """
        url = reverse(self.list_route)
        data = self.invalid_payload
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        """
        Ensure we can update an instance.
        """
        url = reverse(self.detail_route, kwargs={"pk": self.init_item.pk})
        response = self.client.put(url, self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.model.objects.get(pk=self.init_item.pk).name,
            self.valid_payload["name"],
        )

    def test_invalid_update(self):
        """
        Ensure we can not update an instance with invalid payload.
        """
        url = reverse(self.detail_route, kwargs={"pk": self.init_item.pk})
        response = self.client.put(url, self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list(self):
        """
        Ensure we can list instances.
        """
        url = reverse(self.list_route)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.model.objects.count(), 1)

    def test_valid_delete(self):
        """
        Ensure we can delete an instance.
        """
        url = reverse(self.detail_route, kwargs={"pk": self.init_item.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.model.objects.count(), 0)

    def test_invalid_delete(self):
        """
        Ensure we can not delete an instance with invalid payload.
        """
        url = reverse(self.detail_route, kwargs={"pk": 30})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
