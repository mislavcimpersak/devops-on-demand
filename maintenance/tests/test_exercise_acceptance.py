from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework.test import APIClient


class ExerciseAcceptanceTestCase(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("devops_maintenance")

    def test_case_1(self):
        DATA = {
            "DM_capacity": "20",
            "DE_capacity": "8",
            "data_centers": [
                {"name": "Paris", "servers": "20"},
                {"name": "Stockholm", "servers": "62"},
            ],
        }
        RESULT = {"DE": 8, "DM_data_center": "Paris"}

        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 200
        assert response.json() == RESULT

    def test_case_2(self):
        DATA = {
            "DM_capacity": 6,
            "DE_capacity": 10,
            "data_centers": [
                {"name": "Paris", "servers": 30},
                {"name": "Stockholm", "servers": 66},
            ],
        }
        RESULT = {"DE": 9, "DM_data_center": "Stockholm"}

        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 200
        assert response.json() == RESULT

    def test_case_3(self):
        DATA = {
            "DM_capacity": 12,
            "DE_capacity": 7,
            "data_centers": [
                {"name": "Berlin", "servers": 11},
                {"name": "Stockholm", "servers": 21},
            ],
        }
        RESULT = {"DE": 3, "DM_data_center": "Berlin"}

        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 200
        assert response.json() == RESULT
