from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

from .models import Recipe

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    
class RecipeDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_details.html'
