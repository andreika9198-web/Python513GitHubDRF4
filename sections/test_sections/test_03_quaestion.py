from rest_framework.test import APITestCase
from rest_framework import status

from sections.test_sections.utils import get_member_user, get_test_question


class QuestionTest(APITestCase):
    """Тесты для модели Question."""

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
            # ✅ HTTP, а не HttpP
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создание тестового вопроса
        self.question = get_test_question()

    def test_17_question_list(self):
        """
        Тест получения списка вопросов.
        Проверяет, что в списке есть созданный вопрос.
        """
        response = self.client.get('/question/')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных (с учетом пагинации)
        response_data = response.json()
        self.assertEqual(response_data['results']
                         [0]['question'], 'Test Question')

    def test_18_question_detail(self):
        """
        Тест получения детальной информации о вопросе.
        Проверяет, что данные вопроса соответствуют ожидаемым.
        """
        response = self.client.get(f'/question/{self.question.id}/')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка данных в ответе
        response_data = response.json()
        self.assertEqual(response_data.get('question'), 'Test Question')

    def test_19_question_is_correct(self):
        """
        Тест проверки правильности ответа на вопрос.
        Проверяет, что правильный ответ возвращает True,
        а неправильный - False.
        """
        correct_answer = {
            'member_answer': 'Test Content Title'
        }

        wrong_answer = {
            'member_answer': 'Wrong Title Content'
        }

        # Проверка правильного ответа
        response = self.client.post(
            f'/question/{self.question.id}/',
            correct_answer,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json().get('is_correct'))  # ✅ True

        # Проверка неправильного ответа
        response = self.client.post(
            f'/question/{self.question.id}/',
            wrong_answer,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.json().get('is_correct'))  # ✅ False
