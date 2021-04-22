from django.urls import path
from ..api import views

urlpatterns = [
    path(r'article/', views.article_list),
    path(r'article/<int:pk>/', views.articleView),
]