from django.urls import path
from . import views

urlpatterns =[
    path('',views.PostListView.as_view(),name='list_posts'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
]