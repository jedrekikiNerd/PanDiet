from django.core.exceptions import ValidationError
from django.db import models
from common.models import Tags


class Meal(models.Model):
    VISIBILITY_CHOICES = [
         ('public', 'Public'),
         ('private', 'Private')
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    mass = models.DecimalField(max_digits=5, decimal_places=2)
    tags = models.IntegerField(choices=Tags.choices, default=0)
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)

    def __str__(self):
        return f"{self.name} added by {self.author} ({self.visibility})"

    def clean(self):
        # Sprawdzamy, czy masa jest wi�ksza od zera
        if self.masss <= 0:
            raise ValidationError("Mass must be a positive value")

        # Sprawdzamy, czy widoczno�� jest poprawna
        if self.visibility not in dict(self.VISIBILITY_CHOICES):
            raise ValidationError("Invalid visibility")

    def set_tag(self, tag):
        """ Sets a bitflag by the tag """
        self.tags |= tag

    def unset_tag(self, tag):
        """ Removes a bitflag by the tag """
        self.tags &= ~tag

    def has_tag(self, tag):
        """ Checks if the tag is set """
        return (self.tags & tag) != 0