from rest_framework.test import APITestCase
from rest_framework import status

from sections.test_sections.utils import get_admin_user, get_member_user, get_test_content


class ContentTestAdmin(APITestCase):
    """Тесты для модели Content с правами администратора."""

    def setUp(self):
        """Подготовка тестовых данных."""
        self.user = get_admin_user()

        # Получение JWT токена
        response = self.client.post('/users/token/', {
            'email': self.user.email,
            'password': 'qwerty'
        })
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создание тестового контента
        self.content = get_test_content()

    def test_09_content_create(self):
        """
        Тест создания контента администратором.
        Проверяет, что контент создается с правильными данными.
        """
        data = {
            'section': self.content.section.id,
            'title': 'Test Content Title Create',
            'content': 'Test Content Create',
        }
        response = self.client.post(
            '/content/create/', data=data, format='json')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка данных в ответе
        response_data = response.json()
        self.assertEqual(response_data.get('title'),
                         'Test Content Title Create')
        self.assertEqual(response_data.get('content'), 'Test Content Create')

    def test_10_content_detail(self):
        """
        Тест получения детальной информации о контенте.
        Проверяет, что данные контента соответствуют ожидаемым.
        """
        response = self.client.get(f'/content/{self.content.id}/')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных в ответе
        response_data = response.json()
        self.assertEqual(response_data.get('title'), 'Test Content Title')
        self.assertEqual(response_data.get('content'), 'Test Content')

    def test_11_content_update(self):
        """
        Тест частичного обновления контента (PATCH).
        Проверяет, что только указанное поле обновляется.
        """
        data = {
            'title': 'Test Title Update PATCH'
        }
        response = self.client.patch(
            f'/content/{self.content.id}/update/',
            data=data,
            format='json'
        )

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка обновленных данных
        response_data = response.json()
        self.assertEqual(response_data.get('title'), 'Test Title Update PATCH')

        # Проверка, что другие поля не изменились
        self.assertEqual(response_data.get('content'),
                         'Test Content')  # Должно остаться прежним

    def test_12_content_delete(self):
        """
        Тест удаления контента.
        Проверяет, что контент успешно удаляется и больше не доступен.
        """
        # 1. Удаляем контент
        response = self.client.delete(f'/content/{self.content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # 2. Пытаемся получить удаленный контент (должен быть 404)
        response = self.client.get(f'/content/{self.content.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_13_content_list(self):
        """
        Тест получения списка контента.
        Проверяет, что в списке есть созданный контент.
        """
        response = self.client.get('/content/')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных (с учетом пагинации)
        response_data = response.json()
        self.assertEqual(response_data['results']
                         [0]['title'], 'Test Content Title')


class ContentTestMember(APITestCase):
    """Тесты для модели Content с правами обычного пользователя (MEMBER)."""

    def setUp(self):
        """Подготовка тестовых данных."""
        self.user = get_member_user()

        # Получение JWT токена
        response = self.client.post('/users/token/', {
            'email': self.user.email,
            'password': 'qwerty'
        })
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создание тестового контента
        self.content = get_test_content()

    def test_14_content_create_forbidden(self):
        """
        Тест создания контента пользователем с ролью MEMBER.
        Ожидается ошибка 403 Forbidden (недостаточно прав).
        """
        data = {
            'section': self.content.section.id,
            'title': 'Test Content Title Create',
            'content': 'Test Content Create',
        }

        response = self.client.post(
            '/content/create/', data=data, format='json')

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка сообщения об ошибке
        self.assertEqual(
            response.json().get('detail'),
            'У вас недостаточно прав для выполнения данного действия.'
        )

    def test_15_content_update_forbidden(self):
        """
        Тест обновления контента пользователем с ролью MEMBER.
        Ожидается ошибка 403 Forbidden (недостаточно прав).
        """
        data = {
            'title': 'Test Title Update PATCH'
        }

        response = self.client.patch(
            f'/content/{self.content.id}/update/',
            data=data,
            format='json'
        )

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка сообщения об ошибке
        self.assertEqual(
            response.json().get('detail'),
            'У вас недостаточно прав для выполнения данного действия.'
        )

    def test_16_content_delete_forbidden(self):
        """
        Тест удаления контента пользователем с ролью MEMBER.
        Ожидается ошибка 403 Forbidden (недостаточно прав).
        """
        response = self.client.delete(f'/content/{self.content.id}/delete/')

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка сообщения об ошибке
        self.assertEqual(
            response.json().get('detail'),
            'У вас недостаточно прав для выполнения данного действия.'
        )
