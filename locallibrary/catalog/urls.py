from catalog import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),

]
