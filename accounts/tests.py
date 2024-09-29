from django.test import TestCase
from django.contrib.auth.models import User

class BlogTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="foo", password="bar")
        
        
    def test_account(self):

        user = User.objects.all()[0]
        #print(user)
        self.assertIsInstance(user,User)

    

        