from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,IndexView

urlpatterns = [
    path('', PostList.as_view(), name='new_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='news_detail'),
    path('create/', PostCreateView.as_view(), name='news_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
    path('', IndexView.as_view()),
]