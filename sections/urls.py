from os import path as p

from django.urls import path
from rest_framework.routers import DefaultRouter

from sections.apps import SectionsConfig

from sections.views import (SectionListAPIView, SectionCreateAPIView, SectionRetrieveAPIView, SectionUpdateAPIView,
                            SectionDestroyAPIView,ContentListAPIView, ContentCreateAPIView, ContentRetrieveAPIView,
                            ContentDestroyAPIView,ContentUpdateAPIView)

app_name = SectionsConfig.name

router = DefaultRouter()

section = 'section/'
content = 'content/'
question = 'question/'
create = 'create/'
update = 'update/'
delete = 'delete/'
int_pk = '<int:pk>/'

urlpatterns = [
    # section urlpatterns
    path(p.join(section), SectionListAPIView.as_view(), name='section_list'),
    path(p.join(section, create), SectionCreateAPIView.as_view(), name='section_create'),
    path(p.join(section, int_pk), SectionRetrieveAPIView.as_view(), name='section_detail'),
    path(p.join(section, int_pk, update), SectionUpdateAPIView.as_view(), name='section_update'),
    path(p.join(section, int_pk, delete), SectionDestroyAPIView.as_view(), name='section_delete'),

    # content urlpatterns
    path(p.join(content), ContentListAPIView.as_view(), name='content_list'),
    path(p.join(content, create), ContentCreateAPIView.as_view(), name='content_create'),
    path(p.join(content, int_pk), ContentRetrieveAPIView.as_view(), name='content_detail'),
    path(p.join(content, int_pk, update), ContentUpdateAPIView.as_view(), name='content_update'),
    path(p.join(content, int_pk, delete), ContentDestroyAPIView.as_view(), name='content_delete'),
] + router.urls