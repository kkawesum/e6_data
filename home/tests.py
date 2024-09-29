from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User

class BlogTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="foo", password="bar")
        # print(user)
        Blog.objects.create(user=user,title="1234",blog_text="this is just a sample")
        
    def test_user(self):

        user = User.objects.all()[0]
        #print(user)
        obj = Blog.objects.get(user=user)
        

        self.assertEqual(obj.title,"1234")
        self.assertIsInstance(obj.user,User)
