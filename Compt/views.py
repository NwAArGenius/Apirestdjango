from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status


# Create your views here.
class SignupViews(GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
 
    
class LoginViews(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            response = {
                "message": "succeful login",
                "token": user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
    
    def get(self, request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)