from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
from users.user_serializers import UserSerializer, UserCreateSerializer, UserTokenObtainPairSerializer, UserUpdateSerializer
from sections.permissions import IsModerator, IsSuperuser


class UserListAPIView(ListAPIView):
    """
    Представление для получения списка всех пользователей.
    Доступно только авторизованным пользователям.
    """
    queryset = User.objects.all()  # Запрос ко всем пользователям в БД
    serializer_class = UserSerializer  # Сериализатор для преобразования данных
    permission_classes = (IsAuthenticated, IsSuperuser|IsModerator) # Добавить для ограничения доступа


class UserCreateAPIView(CreateAPIView):
    """
    Представление для регистрации нового пользователя.
    Доступно всем (включая неавторизованных).
    """
    queryset = User.objects.all()  # Запрос ко всем пользователям
    serializer_class = UserCreateSerializer  # Сериализатор для создания пользователя
    permission_classes = [AllowAny]  # Разрешаем доступ всем пользователям


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Представление для просмотра информации о конкретном пользователе.
    Доступно всем (включая неавторизованных).
    """
    queryset = User.objects.all()  # Запрос ко всем пользователям
    serializer_class = UserSerializer  # Сериализатор для отображения данных
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления данных пользователя.
    Доступно всем пользователям (включая неавторизованных).
    """
    queryset = User.objects.all()  # Запрос ко всем пользователям
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
       user = self.request.user
       return User.objects.filter(id=user.id)

class UserDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления пользователя.
    Доступно всем пользователям (включая неавторизованных).
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSuperuser)


class UserTokenObtainPairView(TokenObtainPairView):
    """
    Представление для получения JWT токена.
    Доступно всем пользователям (включая неавторизованных).
    """
    serializer_class = UserTokenObtainPairSerializer
    permission_classes = (AllowAny,)