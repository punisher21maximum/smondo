from django.urls import path
from .views import (
    # PostListView,
    # PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView,
    # UserPostListView,
    #bike
    BikeDeleteView,
    #scooty
    ScootyDeleteView,
    #mobile
    MobileDeleteView,
    #subcat Views
    SubcatListView,
    SubcatDetailView,
    SubcatCreateView,
    SubcatUpdateView,
)
from . import views

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),
    #subcat
    path('<str:model>/new/', SubcatCreateView.as_view(), name='subcat-create'),
    path('<str:model>/', SubcatListView.as_view(), name='subcat-list'), 
    path('<str:model>/<int:pk>/', SubcatDetailView.as_view(), name='subcat-detail'), 
    path('<str:model>/<int:pk>/update/', SubcatUpdateView.as_view(), name='subcat-update'),
    #bike
    path('bikes/<int:pk>/delete/', BikeDeleteView.as_view(), name='bikes-delete'),
    #scooty
    path('scootys/<int:pk>/delete/', ScootyDeleteView.as_view(), name='scootys-delete'),
    #mobile
    path('mobiles/<int:pk>/delete/', MobileDeleteView.as_view(), name='mobiles-delete'),
   
]