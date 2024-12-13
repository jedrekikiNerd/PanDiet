from django.core.exceptions import ValidationError
from django.db import models
from users.models import User
from products.models import Product


class Meal(models.Model):
    VISIBILITY_CHOICES = [
         ('public', 'Public'),
         ('private', 'Private')
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    recipe = models.TextField(blank=True)
    mass = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    
    products = models.ManyToManyField(Product, through='MealProducts')

    def __str__(self):
        return f"{self.name} added by {self.author} ({self.visibility})"

    def clean(self):
        # Sprawdzamy, czy masa jest wi�ksza od zera
        if self.mass <= 0:
            raise ValidationError("Mass must be a positive value")

        # Sprawdzamy, czy widoczno�� jest poprawna
        if self.visibility not in dict(self.VISIBILITY_CHOICES):
            raise ValidationError("Invalid visibility")


class MealProducts(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.meal.name} - {self.product.name}"