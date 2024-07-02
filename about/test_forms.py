from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Raymond',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_contains_name(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form name field incomplete")

    def test_form_contains_email(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Raymond',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form email field incomplete")

    def test_form_contains_message(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Raymond',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form message field incomplete")

