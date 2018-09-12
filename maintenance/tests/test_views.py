from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework.test import APIClient


class DevOpsNeedsViewTestCase(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("devops_maintenance")

    def test_get_request(self):
        response = self.client.get(self.url)

        assert response.status_code == 405

    def test_missing_post_body(self):
        response = self.client.post(self.url)

        assert response.status_code == 400

    def test_missing_DM_capacity(self):
        DATA = {
            "DE_capacity": 10,
            "data_centers": [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}],
        }
        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 400
        assert response.json()["DM_capacity"]

    def test_missing_DE_capacity(self):
        DATA = {
            "DM_capacity": 10,
            "data_centers": [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}],
        }
        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 400
        assert response.json()["DE_capacity"]

    def test_missing_data_centers(self):
        DATA = {"DM_capacity": 10, "DE_capacity": 7}
        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 400
        assert response.json()["data_centers"]

    def test_negative_DM_capacity(self):
        DATA = {
            "DM_capacity": -10,
            "DE_capacity": 10,
            "data_centers": [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}],
        }
        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 400
        assert response.json()["DM_capacity"]

    def test_negative_DE_capacity(self):
        DATA = {
            "DM_capacity": 10,
            "DE_capacity": -10,
            "data_centers": [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}],
        }
        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 400
        assert response.json()["DE_capacity"]

    def test_one_data_centers(self):
        DATA = {
            "DM_capacity": 10,
            "DE_capacity": 7,
            "data_centers": [{"name": "Foo", "servers": 20}],
        }
        RESULT = {"DE": 2, "DM_data_center": "Foo"}

        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 200
        assert response.json() == RESULT

    def test_two_data_centers(self):
        DATA = {
            "DM_capacity": 7,
            "DE_capacity": 10,
            "data_centers": [{"name": "Foo", "servers": 20}, {"name": "Bar", "servers": 12}],
        }
        RESULT = {"DE": 3, "DM_data_center": "Bar"}

        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 200
        assert response.json() == RESULT

    def test_three_data_centers(self):
        DATA = {
            "DM_capacity": 7,
            "DE_capacity": 10,
            "data_centers": [
                {"name": "Foo", "servers": 20},
                {"name": "Bar", "servers": 12},
                {"name": "Baz", "servers": 47},
            ],
        }
        RESULT = {"DE": 8, "DM_data_center": "Bar"}

        response = self.client.post(self.url, data=DATA, format="json")

        assert response.status_code == 200
        assert response.json() == RESULT
