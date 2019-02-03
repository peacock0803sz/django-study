from django.urls import path
from django.shortcuts import render, get_object_or_404

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<link.pk/>', views.post_dateil, name='post_dateil')
]


def post_dateil(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_dateil.html', {'post': post})
