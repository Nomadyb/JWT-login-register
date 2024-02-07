from rest_framework import serializers
from .models import User

#yapılacak işlemler
"""
burada rest içinde model serializer oluşturuldu
amaç rest api üzerinden kullanıcı bilgilerini almak ve kaydetmek(JSON formatında)

"""
#TODO: meta yapısını kullanmamalısın manuel ekle 


# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=100)
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'role']



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=70)
    role = serializers.CharField(max_length=100)

