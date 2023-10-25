from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Comment


# These tests first create an Article and Comment, then check
# relevent fields have been created successfully

class ArticleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                        username='testuser', password='testpassword')
        self.article = Article.objects.create(
            title='Test Article',
            slug='test-article',
            author=self.user,
            content='This is the test content.',
            status=1,
        )
        self.comment = Comment.objects.create(
            post=self.article,
            name='Test Commenter',
            email='test@example.com',
            body='This is a test comment.',
        )

    def test_article_model(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.author, self.user)
        self.assertEqual(self.article.content, 'This is the test content.')
        self.assertEqual(self.article.status, 1)

    def test_comment_model(self):
        # correctly link the comment to the article
        self.assertEqual(self.comment.post, self.article)
        self.assertEqual(self.comment.name, 'Test Commenter')
        self.assertEqual(self.comment.body, 'This is a test comment.')
