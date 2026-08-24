from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, Content
from sections.serializers.content_serializers import ContentSectionSerializer

class SectionSerializer(ModelSerializer):
    """
    Полный сериализатор для модели Section.
    Используется для создания, обновления и детального просмотра разделов.
    Возвращает все поля модели Section.
    """
    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    """
    Сериализатор для списка разделов с дополнительной информацией о контенте.
    Используется для отображения списка всех разделов с краткой информацией
    о содержимом каждого раздела.
    """
    section_content_title = SerializerMethodField()

    def get_section_content_title(self, section):
        """
        Возвращает список контента, принадлежащего данному разделу.
        """
        return ContentSectionSerializer(Content.objects.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'section_content_title')