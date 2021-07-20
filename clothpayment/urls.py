from django.urls import path
from .views import *
from knox import views as knox_views

urlpatterns = [
    
    # register / login / logout
    path('register/',RegisterAPI.as_view(),name='register'),
    path('login/',LoginAPI.as_view(),name='login'),    
    path('logout/',knox_views.LogoutView.as_view(),name='logout'),

    # cloth
    path('clothlist/',ClothList.as_view(),name="clothlist"),

    # cart
    path("carts/",CartList.as_view(),name="carts"),
    path("carts/<int:pk>",CartDetail.as_view()),

    # order
    path('orders/', OrderList.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='orderDetails'),
]