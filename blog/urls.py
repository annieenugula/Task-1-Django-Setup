from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('register/', views.register_view, name='register'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('category/<slug:slug>/', views.CategoryPostsView.as_view(), name='category_posts'),
]