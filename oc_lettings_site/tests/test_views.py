from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
