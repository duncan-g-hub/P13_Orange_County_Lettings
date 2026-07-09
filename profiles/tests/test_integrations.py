from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_access_profiles_from_home_page(client, profile_test):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert reverse("profiles_index") in response.content.decode()

    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200
    assert profile_test in response.context["profiles_list"]


@pytest.mark.django_db
def test_access_profile_details_from_profiles_page(client, profile_test):
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assert (reverse("profile", args=[profile_test.user.username])
            in response.content.decode())

    response = client.get(reverse("profile", args=[profile_test.user.username]))
    assert response.status_code == 200
    assert profile_test.user.username in response.content.decode()
    assert profile_test.favorite_city in response.content.decode()
