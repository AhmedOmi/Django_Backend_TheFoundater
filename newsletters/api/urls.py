from django.urls import path
from ..api import views

urlpatterns = [
    path(r'newsletter/', views.Newsletter_list),
    path(r'newsletter/<int:pk>/', views.NewsletterView),
]