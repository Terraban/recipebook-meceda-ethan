from django.urls import path
from .views import RecipesListView, RecipeDetailsView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetailsView.as_view(), name='recipe_details')
]

app_name = 'ledger'