from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_access_lettings_from_home_page(client, letting_test):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert reverse("lettings_index") in response.content.decode()

    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert letting_test in response.context["lettings_list"]


@pytest.mark.django_db
def test_access_letting_details_from_lettings_page(client, letting_test):
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assert reverse("letting", args=[letting_test.id]) in response.content.decode()

    response = client.get(reverse("letting", args=[letting_test.id]))
    assert response.status_code == 200
    assert letting_test.title in response.content.decode()
    assert str(letting_test.address) in response.content.decode()
