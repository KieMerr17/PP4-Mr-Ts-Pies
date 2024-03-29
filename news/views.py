from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, JsonResponse
from .models import Article, Comment
from .forms import CommentForm


# Register Article with news.html
class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('created_on')
    template_name = 'news.html'
    paginate_by = 3


# Function to load Article details
class ArticleDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        liked = False

        # Check if article is liked
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Load and input all comments for article
        comment_form = CommentForm(initial={'name': request.user.username})
        comments = article.comments.all()

        return render(
            request,
            "news_detail.html",
            {
                "article": article,
                "liked": liked,
                "comment_form": comment_form,
                "comments": comments,
            }
        )


# Function for adding comments to articles
def ArticleComment(request, slug):

    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = article
            comment.save()
            url = reverse(
                    'news_detail', kwargs={'slug': slug}) + '#comments-box'
            return redirect(url)
    else:
        comment_form = CommentForm()

    url = reverse('news_detail', kwargs={'slug': slug}) + '#comments-box'
    return redirect(url)


# function to delete users comments
def delete_comment(request, comment_id, slug):
    article = get_object_or_404(Article, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.delete()
        # Refresh page
        url = reverse('news_detail', kwargs={'slug': slug}) + '#comments-box'
        return redirect(url)


# function to handle likes for registered users
class ArticleLike(View):

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
            liked = False
        else:
            article.likes.add(request.user)
            liked = True

        url = reverse('news_detail', kwargs={'slug': slug}) + '#like_count'
        return redirect(url)
