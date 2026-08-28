from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from users.models import User
from users.validators import PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'last_name', 'first_name',
                  'phone_number', 'is_active')


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, min_length=8, max_length=16)

    class Meta:
        model = User
        fields = ('email', 'password')
        validators = [
            PasswordValidator(field='password'),
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')  # Извлекаем пароль
        user = User.objects.create_user(
            password=password,  # create_user сам хеширует
            **validated_data
        )
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name',
                  'phone_number', 'is_active')


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
