from django.contrib import admin
from .models import Wizard, Wand, Spell, Photo

# Register your models here.

admin.site.register(Wizard)
admin.site.register(Wand)

admin.site.register(Spell)
admin.site.register(Photo)