from django.test import TestCase


#pip install coverage
#coverage report
#coverage run manage.py test

from .models import Post
class ModelTesting(TestCase):
    
    def setUp(self) -> None:
        self.blog = Post.objects.create(title='Blog', content='This is a blog')
    
    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(self.blog.title, 'Blog')
        self.assertEqual(self.blog.content, 'This is a blog')
        self.assertEqual(str(self.blog), 'Blog')