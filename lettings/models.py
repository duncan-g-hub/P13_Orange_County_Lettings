"""Models for the lettings app."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Represents an address."""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Manage plural names"""
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        """Return the address as a string."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Represents a letting."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """Manage plural names"""
        verbose_name = "letting"
        verbose_name_plural = "lettings"

    def __str__(self):
        """Return the letting title."""
        return self.title
