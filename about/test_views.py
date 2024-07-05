from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About 

class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title='About Me', content='About content text is here.'
        )
        self.about_content.save()

    def test_render_about_me_view_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertIn(b'About Me', response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_form_submission(self):
        """Test for submitting a collaboration form"""
        # anyone can submit, not just users
        post_data = {
            'name': 'Test Name',
            'email': 'test@test.com',
            'message': 'Test Message'
        }
        response = self.client.post(reverse('about'), post_data )
        # assert (check)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Message sent successfully, I aim to respond in two working days.', response.content
        )
