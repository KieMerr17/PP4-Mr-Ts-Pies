from django.test import TestCase
from django.urls import reverse, resolve
from .views import ArticleList, ArticleLike, ArticleComment, delete_comment


# These tests check that the Article urls are correct and that the
# link once liking, commenting and deleting a comment is also correct

class TestUrls(TestCase):
    def test_article_list_url_resolves(self):
        url = reverse('news')
        self.assertEquals(resolve(url).func.view_class, ArticleList)

    def test_article_like_url_resolves(self):
        url = reverse('article_like', args=['test-article'])
        self.assertEquals(resolve(url).func.view_class, ArticleLike)

    def test_article_comment_url_resolves(self):
        url = reverse('article_comment_add', args=['test-article'])
        self.assertEquals(resolve(url).func, ArticleComment)

    def test_delete_comment_url_resolves(self):
        url = reverse('delete_comment', args=[1, 'test-article'])
        self.assertEquals(resolve(url).func, delete_comment)
