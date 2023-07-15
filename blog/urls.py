from django.urls import path, reverse_lazy
from .views import (
                    BlogListView,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView,

                    ReviewCreateView,
                    ReviewDeleteView,
                    )


app_name='blog'
urlpatterns=[
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), # new
    path('post/new/', BlogCreateView.as_view(), name='post_new'), # new
    path("post/",BlogListView.as_view(),name="main"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new



    path('post/<int:pk>/review', 
        ReviewCreateView.as_view(), name='post_review_create'),
    path('review/<int:pk>/delete',
        ReviewDeleteView.as_view(success_url=reverse_lazy('blog:post_detai')), name='post_review_delete'),
]




