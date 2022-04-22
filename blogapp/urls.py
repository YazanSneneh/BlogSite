from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:pk>', views.article_details, name="article_details"),
    path('delete/<int:pk>', views.delete_post, name="delete_post"),
    path("new/", views.post_new, name='post_new'),
    path("edit/<int:pk>", views.UpdatePost.as_view() ,name="post_edit")
]