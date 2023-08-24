from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='news'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='news_detail'),
    path('article/<slug:slug>/add_comment/', views.ArticleComment, name='article_comment_add'),
    path('delete_comment/<int:comment_id>/<slug:slug>/', views.delete_comment, name='delete_comment'),
]