from django.contrib import admin

from sections.models import Section, Content

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    ordering = ('id',)
    search_fields = ('title',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'title')
    list_filter = ('section',)
    ordering = ('section', 'id')
    search_fields = ('title',)
