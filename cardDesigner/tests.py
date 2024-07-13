from django.test import TestCase
from . models import Post

class ModelTesting(TestCase):
    def setUp(self):
        self.languages = Post.objects.create(
            name = 'Python', author='python', slug='python',
            description = 'Python is a high-level, general-purpose programming language.',
            age = 20
        )
        def test_model(self):
            d = self.languages
            self.assertTrue(isinstance(d, Post))
            self.assertEqual(d.name, 'Python')