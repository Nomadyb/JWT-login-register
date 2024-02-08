from rest_framework import serializers
from .models import User

#yapılacak işlemler
"""
burada rest içinde model serializer oluşturuldu
amaç rest api üzerinden kullanıcı bilgilerini almak ve kaydetmek(JSON formatında)

"""
#TODO: meta yapısını kullanmamalısın manuel ekle 
#TODO: veriler doğrul


# class UserSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=100)
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'role']



class UserSerializer(serializers.Serializer):
    # def __init__(self,id,username,email,role):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=70)
    role = serializers.CharField(max_length=100)

    #verilerin doğrulanmasına bağlı olarak nesnelerin döndürülmesi için hem create hem update uygulanmalıdır
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance

