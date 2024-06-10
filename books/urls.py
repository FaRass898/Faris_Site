from django.urls import path
from . import views


urlpatterns = [
    path('books_catalog', views.books_list_view),
    path('books_catalog/<int:id>/', views.books_detail_view),

    path('personal_info/', views.personal_info_view, name='personal_info'),
    path('hobby/', views.hobby_view, name='hobby'),
    path('current_time/', views.current_time_view, name='current_time'),
    path('random_numbers/', views.random_numbers_view, name='random_numbers'),
]
