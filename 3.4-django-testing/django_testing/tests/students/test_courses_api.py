import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def url():
    return reverse('courses-list')


@pytest.mark.django_db
def test_get_course(client, url, course_factory):
    course = course_factory()
    response = client.get(url + f'{course.id}/')
    data = response.json()
    assert response.status_code == 200
    assert course.name == data['name']


@pytest.mark.django_db
def test_get_courses(client, url, course_factory):
    courses = course_factory(_quantity=100)
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id_courses(client, url, course_factory):
    courses = course_factory(_quantity=50)
    i = 10
    response = client.get(url, {'id': courses[i].id})
    data = response.json()
    assert response.status_code == 200
    assert courses[i].id == data[0]['id']


@pytest.mark.django_db
def test_filter_name_courses(client, url, course_factory):
    courses = course_factory(_quantity=60)
    i = 15
    response = client.get(url, {'name': courses[i].name})
    data = response.json()
    assert response.status_code == 200
    assert courses[i].name == data[0]['name']


@pytest.mark.django_db
def test_create_course(client, url):
    count = Course.objects.count()
    response = client.post(url, data={'name': 'Test course'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, url, course_factory):
    course = course_factory()
    response = client.patch(url + f'{course.id}/', data={'name': 'Test course'})
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data['name'] == 'Test course'


@pytest.mark.django_db
def test_destroy_course(client, url, course_factory):
    course = course_factory()
    response = client.delete(url + f'{course.id}/')
    assert response.status_code == 204
