import pytest
from django.test import Client
from lettings.models import Letting, Address

@pytest.fixture
def client():
    return Client()


@pytest.fixture
def letting_test():
    address = Address.objects.create(
        number=10,
        street="Test Street",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA",
    )

    letting = Letting.objects.create(
        title="Test Letting",
        address=address,
    )
    return letting