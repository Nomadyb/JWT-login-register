from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer




# amaç HTTP iseğini işlemek
# orm modeli üzerinden tanımla serializer hepsini kayıt etme 
# try except ile hata yakalama
# serializer.data için olan olmayan veri için hata mesajı döndürme
""" class RegisterView(APIView):
    permission_classes = [AllowAny] # tüm izinler verilir çünkü amaç herhangi birinin kayıt olmasıdır

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # user kayıt olduktan sonra objesi döndürülür
            #User.objects.filter(id=user.id).update(is_active=True) 
            #tokenı döndürme
            refresh = RefreshToken.for_user(user)
            return Response({
                'isSuccess': True,
                'message': 'Registration successful',
                'data': serializer.data,
                
                'token': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            'isSuccess': False,
            'message': 'Registration failed',
            'errors': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
 """






class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            username = request.data.get('username')
            email = request.data.get('email')
            role = request.data.get('role')

            if not (username and email):
                return Response({
                    'isSuccess': False,
                    'message': 'Registration failed',
                    'errors': {'detail': 'Both username and email are required.'}
                }, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return Response({
                    'isSuccess': False,
                    'message': 'Registration failed',
                    'errors': {'detail': 'Username or email is already taken.'}
                }, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                username=username, email=email, role=role)
            user.is_active = True
            user.save()

            return Response({
                'isSuccess': True,
                'message': 'Registration successful',
                'data': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'role': user.role,
                },
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'isSuccess': False,
                'message': 'An error occurred during registration',
                'error': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#TODO: kullanıcı girişi için token yapısına bak
#TODO: hata yapılarına bak 


#kullanıcı girişi token gerekiyor sanırsam
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

