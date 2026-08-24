from rest_framework.pagination import PageNumberPagination


class SectionPagination(PageNumberPagination):
    """
    Пагинация для разделов (Section).

    - page_size: 3 записи на страницу по умолчанию
    - page_size_query_param: параметр для изменения размера страницы (?page_size=5)
    - max_page_size: максимальное количество записей на странице (10)
    """
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class ContentPagination(SectionPagination):
    """
    Пагинация для контента (Content).
    Наследуется от SectionPagination, изменяет только размер страницы.

    - page_size: 5 записей на страницу по умолчанию
    """
    page_size = 5