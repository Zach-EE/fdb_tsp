from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import IndexView

class IndexPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)
        
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_indexpage_url_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(self.response.status_code, 200)
        
    def test_indexpage_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
        
    def test_indexpage_contains_correct_html(self):
        self.assertContains(self.response, 'index page')
        
    def test_indexpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'this should not be there')
        
    def test_indexpage_url_resolves_indexpageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, IndexView.as_view().__name__)