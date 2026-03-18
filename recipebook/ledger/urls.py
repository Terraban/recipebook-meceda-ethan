from django.urls import path
from .views import RecipesListView, RecipeDetailsView, RecipeAddView, RecipeAddImageView

urlpatterns = [
    path('recipes/list', RecipesListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetailsView.as_view(), name='recipe_details'),
    path('recipe/add', RecipeAddView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/add_image', RecipeAddImageView.as_view(), name='recipe_add_image')
]

app_name = 'ledger'