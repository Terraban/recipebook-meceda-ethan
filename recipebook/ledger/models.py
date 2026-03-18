from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from useraccount.models import Profile

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_details', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(
        Profile,
        on_delete = models.CASCADE,
        related_name = 'recipes'
    )
    
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_details', args=[str(self.id)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete = models.CASCADE,
        related_name = 'recipe'
    )
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        related_name = 'ingredients'
    )
    
class RecipeImage(models.Model):
    recipe_image = models.ImageField(upload_to='images/', null = False)
    description = models.CharField(max_length=255)
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        related_name = 'images'
    )