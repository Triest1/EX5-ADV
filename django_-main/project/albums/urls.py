from django.urls import path
from .views import TagListCreateView, CategoryListCreateView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
     path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]
