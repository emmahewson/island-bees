from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """ Message Model """

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages"
    )

    name = models.CharField(
        max_length=50,
        null=True,
        blank=False
    )

    email = models.EmailField(
        max_length=254,
        null=True,
        blank=False
    )

    subject = models.CharField(
        max_length=40,
        blank=False,
        null=False
    )

    content = models.TextField(
        max_length=500
    )

    created_on = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False
    )

    is_open = models.BooleanField(
        default=True
    )

    def __str__(self):
        """ String representation of Review title """
        return self.subject
