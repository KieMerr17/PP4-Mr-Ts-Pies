from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='news'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='news_detail'),
]