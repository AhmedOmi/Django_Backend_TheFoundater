from django.urls import path
from ..api import views

urlpatterns = [
    path(r'contact/', views.Contact_list),
    path(r'contact/<int:pk>/', views.ContactView),
]