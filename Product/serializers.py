from rest_framework.serializers import ModelSerializer
from .models import Category, Product,Cart,CartItem
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import serializers


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
        
class ProfuctSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationErrors('category already exites')
        return value
    
    
class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        



    