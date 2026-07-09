import pytest
from django.test import Client
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def client():
    return Client()



@pytest.fixture
def user_test():
    user = User.objects.create_user(
        username="Test User",
        password="PasswordTest01",
        first_name="Test",
        last_name="TESTUSER",
        email="email@test.com"
    )
    return user


@pytest.fixture
def profile_test(user_test):
    profile = Profile.objects.create(
        user=user_test,
        favorite_city="Test City"
    )
    return profile



