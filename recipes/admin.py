from django.contrib import admin

# Register your models here.
from recipes.models import Recipes

admin.site.register(Recipes)
