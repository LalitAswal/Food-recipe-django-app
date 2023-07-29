from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_userEmail_successful(self):
        """ Test to create user and email successfully """
        email = 'lalit.aswal@gmail.com'
        password = 'checking123'
        user = get_user_model().objects.create_user(
                email=email,
                password=password
            )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        """ testing  email for new user is normalized """    
        email = 'lalit.aswal@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test email for new user if invalid raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_superuser_create(self):
        """test to create super user"""
        user_name = 'lalit.aswal@gmail.com'
        password = 'lalit123'

        user = get_user_model().objects.create_superuser(
            user_name,
            password
            ) 