from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Section, Content
class ContentSerializer(ModelSerializer):
    """
    Сериализатор для модели Content.
    Используется для полного CRUD (создание, чтение, обновление, удаление) контента.
    Возвращает все поля модели.
    """
    class Meta:
        model = Content
        fields = '__all__'


class ContentSectionSerializer(ModelSerializer):
    """
    Сериализатор для краткого представления контента в составе раздела.
    Используется для отображения списка материалов внутри раздела.
    Возвращает только ID и заголовок контента.
    """
    class Meta:
        model = Content
        fields = ('id', 'title')


class ContentListSerializer(ModelSerializer):
    """
    Сериализатор для списка контента с информацией о разделе.
    Используется для отображения списка всех материалов с указанием названия раздела.
    Возвращает ID, название раздела и заголовок контента.
    """
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Content
        fields = ('id', 'section', 'title')