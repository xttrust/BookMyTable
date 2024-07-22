from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class PagesViewsTest(TestCase):
    def setUp(self):
        """
        Set up user and initial data for view testing.
        Create a user and log them in for view testing.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_home_page_view(self):
        """
        Test the home page view.
        Ensure the view responds with status code 200, uses the correct template,
        and includes specific content in the response.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertContains(response, 'BookMyTable')

    def test_about_page_view(self):
        """
        Test the about page view.
        Ensure the view responds with status code 200, uses the correct template,
        and includes specific content in the response.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertContains(response, 'About Us')


