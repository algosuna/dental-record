from django.db import models


class TimeStampedModel(models.Model):
    ''' Adds a timestamp to the created date and the modified date of the model.
    Abstract model to add wherever. '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CancelledModel(models.Model):
    ''' Should be used when a model has the option of getting cancelled. '''
    created_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    class Meta:
        abstract = True
