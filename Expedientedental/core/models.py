from django.db import models

class Grupo(models.Model):
    """The name and number which a patient belongs to.
    Used throughout the project."""

    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)

class TimeStampedModel(models.Model):
    """Adds a timestamp to the created date and the modified date of the model.
    Abstract model to add wherever."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True



