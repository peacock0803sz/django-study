from django.urls import path
from django.shortcuts import render, get_object_or_404

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<link.pk>/', views.post_detail, name='post_detail')
]


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
