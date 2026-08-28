from users.models import User, UserRoles
from sections.models import Section, Content, Question


def get_admin_user():
    """Создает тестового администратора."""
    user = User.objects.create(
        email='tester_admin@test1.com',
        role=UserRoles.ADMIN,
        is_superuser=True,
        is_staff=True,
        is_active=True,
    )
    user.set_password('qwerty')
    user.save()
    return user


def get_member_user():
    """
    Создает и возвращает тестового пользователя с ролью MEMBER.
    Используется в тестах для проверки доступа обычных пользователей.
    """
    user = User.objects.create(
        email='tester_member@test1.com',
        role=UserRoles.MEMBER,
        is_superuser=False,
        is_staff=False,
        is_active=True,
    )
    user.set_password('qwerty')
    user.save()
    return user


def get_test_section():
    """Создает тестовый раздел."""
    section = Section.objects.create(
        title='Test Section',
        description='Test Description',
    )
    return section


def get_test_content():
    """Создает тестовый контент, связанный с тестовым разделом."""
    section = get_test_section()
    content = Content.objects.create(
        section=section,
        title='Test Content Title',
        content='Test Content',
    )
    return content


def get_test_question():
    """Создает тестовый вопрос для использования в тестах."""
    content = get_test_content()
    question = Question.objects.create(
        section=content.section,
        description='Test Question Description',
        question='Test Question',
        answer=content,
    )
    return question
