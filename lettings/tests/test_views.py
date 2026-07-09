from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client, letting_test):
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')
    assert letting_test in response.context["lettings_list"]


@pytest.mark.django_db
def test_letting_view(client, letting_test):
    response = client.get(reverse("letting", args=[letting_test.id]))
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')
    assert response.context["title"] == letting_test.title
    assert response.context["address"] == letting_test.address


@pytest.mark.django_db
def test_letting_view_returns_404(client):
    response = client.get(reverse("letting", args=["999"]))
    assert response.status_code == 404
