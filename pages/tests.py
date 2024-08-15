from django.test import TestCase, SimpleTestCase

class HomePageTests(SimpleTestCase):
    def test_url_exists_at_current_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_current_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
# Create your tests here.
