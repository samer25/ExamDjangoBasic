from django.shortcuts import render, redirect

# Create your views here.
from recipes.forms import FormRecipes
from recipes.models import Recipes


def home_page(req):
    recipes = Recipes.objects.all()
    return render(req, 'index.html', {'recipes': recipes})


def create(req):
    if req.method == 'GET':
        form = FormRecipes()
        return render(req, 'create.html', {'form': form})
    else:
        form = FormRecipes(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(req, 'create.html', {'form': form})


def edit(req, pk):
    recipes = Recipes.objects.get(pk=pk)
    if req.method == 'GET':
        form = FormRecipes(instance=recipes)
        return render(req, 'edit.html', {'form': form})
    else:
        form = FormRecipes(req.POST, instance=recipes)
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(req, 'edit.html', {'form': form})


def delete(req, pk):
    recipes = Recipes.objects.get(pk=pk)
    if req.method == 'GET':
        form = FormRecipes(instance=recipes)
        form.fields['title'].widget.attrs['readonly'] = True
        form.fields['images_url'].widget.attrs['readonly'] = True
        form.fields['description'].widget.attrs['readonly'] = True
        form.fields['ingredients'].widget.attrs['readonly'] = True
        form.fields['time'].widget.attrs['readonly'] = True
        return render(req, 'delete.html', {'form': form})
    else:
        recipes.delete()
        return redirect('home page')


def details(req, pk):
    recipes = Recipes.objects.get(pk=pk)
    ingredients = recipes.ingredients.split(", ")
    context = {
        'recipes': recipes,
        'ingredients': ingredients,
        'pk': pk,

    }
    return render(req, 'details.html', context)
