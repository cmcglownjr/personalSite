from django.test import SimpleTestCase
from django.urls import reverse


class HomeTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("base:home"))
        self.assertEquals(response.status_code, 200)
