from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeImage

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    
class RecipeDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_details.html'
    
class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_add.html'
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipes_list')  

class RecipeAddImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'recipe_add_image.html'
    form_class = RecipeImageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(pk = self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe_details', 
            kwargs={'pk': self.object.recipe.pk }
        )
    
def recipe_add(request):
    form = RecipeForm()

    ctx = {
        "form": form
    }

    if request.method== 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'recipe_add.html', ctx)

def recipe_add_image(request):
    form = RecipeImageForm()

    ctx = {
        "form": form
    }

    if request.method== 'POST':
        form = RecipeImageForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'recipe_add_image.html', ctx)

