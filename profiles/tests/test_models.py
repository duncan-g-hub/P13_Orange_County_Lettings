import pytest
from profiles.models import Profile


@pytest.mark.django_db
def test_model_profile(profile_test):
    assert str(profile_test) == profile_test.user.username


@pytest.mark.django_db
def test_model_profile_meta():
    assert Profile._meta.verbose_name == "profile"
    assert Profile._meta.verbose_name_plural == "profiles"


@pytest.mark.django_db
def test_models_profile_user_relation(profile_test):
    assert profile_test.user.pk == profile_test.user_id