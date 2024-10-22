from django.contrib import admin
from .models import FoodItem, NutritionCategory, Nutrition

admin.site.register(FoodItem)
admin.site.register(NutritionCategory)
admin.site.register(Nutrition)
