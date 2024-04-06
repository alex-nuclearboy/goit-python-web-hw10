from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='index'),
    path('tag/', views.add_tag, name='add_tag'),
    path('author_form/', views.add_author, name='add_author'),
    path('author/<int:author_id>', views.author_detail, name='author_detail'),
    path('author/edit/<int:author_id>/', views.edit_author, name='edit_author'),
    path('quote_form/', views.add_quote, name='add_quote'),
    path('quote/edit/<int:quote_id>/', views.edit_quote, name='edit_quote'),
    path('tag/<int:tag_id>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('quote/delete/<int:quote_id>/', views.delete_quote, name='delete_quote'),
]
