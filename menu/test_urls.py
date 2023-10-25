from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import PieList, PieLike

# These tests check that the pies url is correct and that the link once liking
# a pie is also correct


class TestUrls(SimpleTestCase):
    def test_pie_list_url_resolves(self):
        url = reverse('pies')
        self.assertEquals(resolve(url).func.view_class, PieList)

    def test_pie_like_url_resolves(self):
        url = reverse('pie_like', args=['test-pie'])
        self.assertEquals(resolve(url).func.view_class, PieLike)
