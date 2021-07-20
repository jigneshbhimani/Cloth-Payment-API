from django.shortcuts import render
from .serializers import ClothSerializer, RegisterSerializer, UserSerializer, CartSerializer, OrderSerializer
from .models import Cloth, Cart, Order
from rest_framework.generics import ListAPIView
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
import stripe

# Create your views here.

# -------------------Register-----------------

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        # Check If our serializer is valid or not?
        serializer.is_valid(raise_exception=True)
        # If our serializer is valid then we are going to save serializer
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# -----------------Login------------------------

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        # Check If our serializer is valid or not?
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # create session based authentication with token based authentication
        login(request,user)
        return super(LoginAPI,self).post(request,format=None)

# ---------------Cloth-----------------------

class ClothList(ListAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer


# ----------------Cart-----------------------

class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



# ---------------------Order----------------------------

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# ---------------------Payment---------------------------

# stripe.api_key = "pk_test_51J8J6pSIIkglpNEV5DvCWLA9xNSLN3WeYUzHZrVzbrRcjz7sVvP4wZ5nYZzIVpIBKR6EpUM4IZO4Vd3ux76Rt34800sRhUy8aI"

# stripe.Charge.create(
#     amount = 500,
#     currency = "INR",
#     source = "tok_visa",
#     description = "Payment",
#     payment_method_types=['card'],
#     stripe_account='{{acct_1J8J6pSIIkglpNEV}}',
# )