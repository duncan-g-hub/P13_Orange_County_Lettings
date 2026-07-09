from django.urls import reverse, resolve

from profiles.views import index, profile


def test_url_index():
    url = reverse('profiles_index')
    assert resolve(url).view_name == 'profiles_index'
    assert resolve(url).func == index


def test_url_profile():
    url = reverse('profile', args=["testuser"])
    assert resolve(url).view_name == 'profile'
    assert resolve(url).func == profile
