from django.contrib import admin
from .models import Exercise, ExerciseLevel, ExerciseCategory, TrainingPlan, TrainingPlanExercise, Schedule

admin.site.register(Exercise)
admin.site.register(ExerciseLevel)
admin.site.register(ExerciseCategory)
admin.site.register(TrainingPlan)
admin.site.register(TrainingPlanExercise)
admin.site.register(Schedule)
