from django.urls import path
from . import views


urlpatterns = [
    path('books_catalog', views.BooksListView.as_view()),
    path('books_catalog/<int:id>/', views.BooksDetailView.as_view()),
    path('books_catalog/<int:id>/delete/', views.BooksDetailView.as_view()),
    path('books_catalog/<int:id>/update/', views.EditBookView.as_view()),
    path('books_catalog/search/', views.SearchListView.as_view(), name='search'),
    path('books_catalog/create_book/', views.CreateBookView.as_view()),


]
