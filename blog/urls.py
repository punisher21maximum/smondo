from django.urls import path
from .views import (
    # PostListView,
    # PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView,
    # UserPostListView,
    #bike
    BikeCreateView,
    BikeListView,  
    BikeDetailView, BikeDetailView2,
    BikeUpdateView,
    BikeDeleteView,
    #scooty
    ScootyCreateView,
    ScootyListView,
    ScootyDetailView,
    ScootyUpdateView,
    ScootyDeleteView,
    #mobile
    MobileCreateView,
    MobileListView,
    MobileDetailView,
    MobileUpdateView,
    MobileDeleteView,
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
    #bikes
    path('bikes/new/', BikeCreateView.as_view(), name='bikes-create'),
    path('bikes/', BikeListView.as_view(), name='bikes-home'),
    path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bikes-detail'),
    path('<str:model>/<int:pk>/', BikeDetailView2.as_view(), name='subcat-detail'),#test-detail
    path('bikes/<int:pk>/update/', BikeUpdateView.as_view(), name='bikes-update'),
    path('bikes/<int:pk>/delete/', BikeDeleteView.as_view(), name='bikes-delete'),
    #scooty
    path('scootys/new/', ScootyCreateView.as_view(), name='scootys-create'),
    path('scootys/', ScootyListView.as_view(), name='scootys-home'),
    path('scootys/<int:pk>/', ScootyDetailView.as_view(), name='scootys-detail'),
    path('scootys/<int:pk>/update/', ScootyUpdateView.as_view(), name='scootys-update'),
    path('scootys/<int:pk>/delete/', ScootyDeleteView.as_view(), name='scootys-delete'),
    #mobile
    path('mobiles/new/', MobileCreateView.as_view(), name='mobiles-create'),
    path('mobiles/', MobileListView.as_view(), name='mobiles-home'),
    path('mobiles/<int:pk>/', MobileDetailView.as_view(), name='mobiles-detail'),
    path('mobiles/<int:pk>/update/', MobileUpdateView.as_view(), name='mobiles-update'),
    path('mobiles/<int:pk>/delete/', MobileDeleteView.as_view(), name='mobiles-delete'),
   
]