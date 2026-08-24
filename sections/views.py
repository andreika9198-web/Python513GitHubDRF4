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
