from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content
from sections.permissions import IsModerator, IsSuperuser
from sections.serializers.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializers.content_serializers import ContentSerializer, ContentSectionSerializer, ContentListSerializer

from sections.paginators import SectionPagination, ContentPagination

class SectionListAPIView(ListAPIView):
    """
    Представление для получения списка всех разделов.
    Доступно всем пользователям (включая неавторизованных).
    Поддерживает пагинацию.
    """
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = SectionPagination


class SectionCreateAPIView(CreateAPIView):
    """
    Представление для создания нового раздела.
    Доступно только авторизованным пользователям с правами модератора или администратора.
    """
    serializer_class = SectionSerializer
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionRetrieveAPIView(RetrieveAPIView):
    """
    Представление для просмотра详细信息 о конкретном разделе.
    Доступно всем пользователям (включая неавторизованных).
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления данных раздела.
    Доступно только авторизованным пользователям с правами модератора или администратора.
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)


class SectionDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления раздела.
    Доступно только авторизованным пользователям с правами модератора или администратора.
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)

class ContentListAPIView(ListAPIView):
    """
    Представление для получения списка всего контента.
    Доступно всем пользователям (включая неавторизованных).
    Поддерживает пагинацию.
    """
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)
    pagination_class = ContentPagination


class ContentCreateAPIView(CreateAPIView):
    """
    Представление для создания нового контента.
    Доступно только авторизованным пользователям с правами модератора или администратора.
    """
    serializer_class = ContentSerializer
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)

class ContentRetrieveAPIView(RetrieveAPIView):
    """
    Представление для просмотра детальной информации о конкретном контенте.
    Доступно всем пользователям (включая неавторизованных).
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated,)

class ContentUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления данных контента.
    Доступно только авторизованным пользователям с правами модератора или администратора.
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperuser)

class ContentDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления контента.
    Доступно только авторизованным суперпользователям.
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsSuperuser)