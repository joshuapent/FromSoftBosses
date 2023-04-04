from django.contrib import admin
from .models import Boss, Game, Weakness, Strengths

# Register your models here.
admin.site.register(Boss)
admin.site.register(Game)
admin.site.register(Weakness)
admin.site.register(Strengths)