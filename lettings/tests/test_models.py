import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_model_address(address_test):
    assert str(address_test) == f"{address_test.number} {address_test.street}"


@pytest.mark.django_db
def test_model_address_meta():
    assert Address._meta.verbose_name == "address"
    assert Address._meta.verbose_name_plural == "addresses"


@pytest.mark.django_db
def test_model_letting(letting_test):
    assert str(letting_test) == f"{letting_test.title}"
    assert (str(letting_test.address) ==
            f"{letting_test.address.number} {letting_test.address.street}")


@pytest.mark.django_db
def test_model_letting_meta():
    assert Letting._meta.verbose_name == "letting"
    assert Letting._meta.verbose_name_plural == "lettings"


@pytest.mark.django_db
def test_models_letting_address_relation(letting_test):
    assert letting_test.address.pk == letting_test.address_id