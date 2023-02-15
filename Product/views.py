from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Product, Category, CartItem, Cart
from rest_framework import status
from .serializers import CategorySerializers, ProfuctSerializers, CartSerializers, CartItemSerializers
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
def categoryView(request):
    try:
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def productViews(request):
    try:
        product = Product.objects.filter(status=True)
        serializer = ProfuctSerializers(product, many=True)
        return Response(serializer.data)
    
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def createdProductViews(request):
    product = Product.objects.all()
    serializer = ProfuctSerializers(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def createdCategoryViews(request):
    category = Category.objects.all()
    serializer = CategorySerializers(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
     
@api_view(['GET', 'PUT', 'DELETE'])
def ProductDtailsViews(request, id):
    try:
        product = Product.objects.get(id=id) 
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfuctSerializers(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProfuctSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET', 'PUT', 'DELETE'])
def categorytDtailsViews(request, id):
    try:
        category = Category.objects.get(id=id) 
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'PUT', 'DELETE']) 
def CartUpdatDetailREmove(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == 'GET':
        serializer = CartSerializers(cart)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CartSerializers(cart, request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_302_FOUND)

    

