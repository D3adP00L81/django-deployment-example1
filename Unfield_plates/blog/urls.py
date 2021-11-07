from django.urls import path

from .views import PostListView,PostExactDetailView

app_name = 'blog'

urlpatterns = [
    path('blog/list/', PostListView.as_view(), name='post-list'),
    path('blog/post/<int:pk>/',PostExactDetailView.as_view(),name='post-exact-detail')
]
