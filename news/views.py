from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('created_on')
    template_name = 'news.html'
    paginate_by = 3


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter (status=1)
        article = get_object_or_404(queryset, slug=slug)
        liked = False

        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "news_detail.html",
            {
                "article": article,
                "liked": liked
            }
        )