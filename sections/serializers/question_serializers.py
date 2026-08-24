from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.fields import CharField

from sections.models import Question, Section

class QuestionSerializer(ModelSerializer):
    """
    Сериализатор для модели Question (базовый).
    Используется для отображения вопроса с названием раздела.
    """
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'question')


class QuestionSectionSerializer(ModelSerializer):
    """
    Сериализатор для модели Question (расширенный).
    Используется для отображения вопроса с названием раздела и ответом пользователя.
    """
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())
    member_answer = CharField()

    class Meta:
        model = Question
        fields = ('id', 'section', 'question', 'member_answer')