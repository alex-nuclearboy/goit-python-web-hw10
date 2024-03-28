from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='index'),
    path('tag/', views.add_tag, name='add_tag'),
    path('author_form/', views.add_author, name='add_author'),
    path('author/<int:author_id>', views.author_detail, name='author_detail'),
    path('quote_form/', views.add_quote, name='add_quote'),
]
