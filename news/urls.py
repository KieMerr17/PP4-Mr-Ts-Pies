from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='news'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='news_detail'),
    path('article/<slug:slug>/add_comment/', views.add_article_comment, name='article_comment_add'),
]