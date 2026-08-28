from rest_framework.test import APITestCase
from rest_framework import status

from sections.test_sections.utils import get_admin_user, get_member_user, get_test_section


class SectionTestsAdmin(APITestCase):
    """
    Тесты для модели Section с правами администратора.
    """

    def setUp(self):
        """Подготовка тестовых данных: создание администратора, получение токена."""
        self.user = get_admin_user()

        # Получение JWT токена
        response = self.client.post(
            '/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создание тестового раздела
        self.test_section = get_test_section()

    def test_01_create_section(self):
        """
        Тест создания раздела.
        Проверяет, что администратор может создать новый раздел.
        """
        data = {
            'title': 'Test Section Create',
            'description': 'Test Description Create',
        }
        response = self.client.post(
            '/section/create/', data=data, format='json')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверка данных в ответе
        self.assertEqual(response.json().get('title'), 'Test Section Create')
        self.assertEqual(response.json().get(
            'description'), 'Test Description Create')

    def test_02_section_detail(self):
        """Тест получения детальной информации о разделе."""
        response = self.client.get(f'/section/{self.test_section.id}/')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных в ответе
        response_data = response.json()
        self.assertEqual(response_data.get('title'), 'Test Section')
        self.assertEqual(response_data.get('description'), 'Test Description')

    def test_03_section_update(self):
        """Тест полного обновления раздела (PUT)."""
        data = {
            'title': 'Test Section Update PUT',
            'description': 'Test Description Update PUT',
        }

        response = self.client.put(
            f'/section/{self.test_section.id}/update/',
            data=data,
            format='json'
        )

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных в ответе
        response_data = response.json()
        self.assertEqual(response_data.get('title'), 'Test Section Update PUT')
        self.assertEqual(response_data.get('description'),
                         'Test Description Update PUT')

    def test_04_section_delete(self):
        """Тест удаления раздела."""
        # Удаление раздела
        response = self.client.delete(
            f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверка, что раздел удален
        response = self.client.get(f'/section/{self.test_section.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_05_section_list(self):
        """Тест получения списка разделов."""
        response = self.client.get('/section/')

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных (с учетом пагинации)
        response_data = response.json()
        self.assertEqual(response_data['results'][0]['title'], 'Test Section')


class SectionTestsMember(APITestCase):
    """Тесты для модели Section с правами обычного пользователя (MEMBER)."""

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
            # ✅ HTTP, а не Http
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создание тестового раздела
        self.test_section = get_test_section()

    def test_06_section_create(self):
        """
        Тест создания раздела пользователем с ролью MEMBER.
        Ожидается ошибка 403 Forbidden (недостаточно прав).
        """
        data = {
            'title': 'Test Section Create',
            'description': 'Test Description Create',
        }
        response = self.client.post(
            '/section/create/', data=data, format='json')

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка сообщения об ошибке
        self.assertEqual(response.json().get(
            'detail'), 'У вас недостаточно прав для выполнения данного действия.')

    def test_07_section_update(self):
        """
        Тест обновления раздела пользователем с ролью MEMBER.
        Ожидается ошибка 403 Forbidden (недостаточно прав).
        """
        data = {
            'title': 'Test Section Update PUT',
            'description': 'Test Description Update PUT',
        }

        response = self.client.put(
            f'/section/{self.test_section.id}/update/',
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

    def test_08_section_delete(self):
        """
        Тест удаления раздела пользователем с ролью MEMBER.
        Ожидается ошибка 403 Forbidden (недостаточно прав).
        """
        response = self.client.delete(
            f'/section/{self.test_section.id}/delete/')

        # Проверка статуса
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Проверка сообщения об ошибке
        self.assertEqual(
            response.json().get('detail'),
            'У вас недостаточно прав для выполнения данного действия.'
        )
