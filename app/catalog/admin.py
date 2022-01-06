from django.contrib import admin

# Register your models here.

from .models import AllWord, Antonym, Synonym, WordStructure

admin.site.register(AllWord)
admin.site.register(Antonym)
admin.site.register(Synonym)
admin.site.register(WordStructure)
