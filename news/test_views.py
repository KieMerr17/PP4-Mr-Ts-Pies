from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Article, Comment
from .views import ArticleList, ArticleDetail, ArticleComment, ArticleLike, delete_comment


# This test first creates an Aricle and a Comment object. It then
# confirms that they can be viewed and associated with the article
# Checks that article can be liked, commented and deleted

class ArticleListViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.article = Article.objects.create(
            title='Test Article',
            slug='test-article',
            author=self.user,
            content='This is a test article content.',
            status=1,
        )
        self.comment = Comment.objects.create(
            post=self.article,
            name='Test Commenter',
            email='test@example.com',
            body='This is a test comment.',
        )
        self.client.login(username='testuser', password='testpassword')

    def test_article_list_view(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        self.assertContains(response, 'Test Article')

    def test_article_detail_view(self):
        response = self.client.get(
                reverse('news_detail', args=[self.article.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_detail.html')
        self.assertContains(response, 'Test Article')
        self.assertContains(response, 'Test Commenter')
        self.assertContains(response, 'This is a test comment.')

    def test_article_like_view(self):
        response = self.client.post(
            reverse('article_like', args=[self.article.slug]))
        self.assertEqual(response.status_code, 302)  # Redirect

    def test_delete_comment_view(self):
        response = self.client.post(
            reverse('delete_comment',
                    args=[self.comment.id, self.article.slug]))
        self.assertEqual(response.status_code, 302)  # Redirect
