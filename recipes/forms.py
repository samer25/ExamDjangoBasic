from django import forms

from recipes.models import Recipes


class FormRecipes(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
