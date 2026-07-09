from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client, profile_test):
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')
    assert profile_test in response.context["profiles_list"]


@pytest.mark.django_db
def test_profile_view(client, profile_test):
    response = client.get(reverse("profile", args=[profile_test.user.username]))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html')
    assert response.context["profile"] == profile_test


@pytest.mark.django_db
def test_profile_view_returns_404(client):
    response = client.get(reverse("profile", args=["unknown_user"]))
    assert response.status_code == 404
