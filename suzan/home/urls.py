from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView,BlogCreateView,BlogUpdateView
urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name="blog-update"),

]
