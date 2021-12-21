from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def setUp(self):
        # Get the user model
        self.user_model = get_user_model()

    def tearDown(self) -> None:
        """Clean up the database."""
        get_user_model().objects.all().delete()

    def test_create_a_user(self):
        # Preparation
        user_email = "test_user@email.com"
        password = "test_pass"
        username = "Andres"

        # Subject under test
        user = self.user_model.objects.create_user(
            username=username, email=user_email, password=password
        )

        # Asserts
        self.assertEqual(user.username, username)
