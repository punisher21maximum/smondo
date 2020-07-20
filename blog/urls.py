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
    BikeUpdateView,
    BikeDeleteView,
    #scooty
    ScootyCreateView,
    ScootyUpdateView,
    ScootyDeleteView,
    #mobile
    MobileCreateView,
    MobileUpdateView,
    MobileDeleteView,
    #subcat Views
    SubcatListView,
    SubcatDetailView,
    SubcatCreateView,
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
    # path('bikes/new/', BikeCreateView.as_view(), name='bikes-create'),
    path('<str:model>/new/', SubcatCreateView.as_view(), name='subcat-create'),
    path('<str:model>/', SubcatListView.as_view(), name='subcat-list'),#test-list
    path('<str:model>/<int:pk>/', SubcatDetailView.as_view(), name='subcat-detail'),#test-detail
    path('bikes/<int:pk>/update/', BikeUpdateView.as_view(), name='bikes-update'),
    path('bikes/<int:pk>/delete/', BikeDeleteView.as_view(), name='bikes-delete'),
    #scooty
    # path('scootys/new/', ScootyCreateView.as_view(), name='scootys-create'),
    path('scootys/<int:pk>/update/', ScootyUpdateView.as_view(), name='scootys-update'),
    path('scootys/<int:pk>/delete/', ScootyDeleteView.as_view(), name='scootys-delete'),
    #mobile
    # path('mobiles/new/', MobileCreateView.as_view(), name='mobiles-create'),
    path('mobiles/<int:pk>/update/', MobileUpdateView.as_view(), name='mobiles-update'),
    path('mobiles/<int:pk>/delete/', MobileDeleteView.as_view(), name='mobiles-delete'),
   
]