from django.contrib.auth import models
from django.db.models import fields
from django.db.models.fields import Field
from .models import Cloth, Cart, Order
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']



# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
    def create(self,validated_date):
        user  = User.objects.create_user(validated_date['username'],validated_date['email'],validated_date['password'])
        return user


# Cloth Serializer
class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = ['id','item','price','created_at']



# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    cart = UserSerializer(many=False)
    clothes = ClothSerializer(many=True)
    class Meta:
        model = Cart
        total = Field('total')
        fields = ['cart','created_at','clothes','quantity','total']


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(many=False)
    class Meta:
        model = Order
        cart_total = Field('cart_total')
        final_total = Field('final_total')
        fields = ['id','cart','created_at','updated_at','shipping_charge','cart_total','final_total']


