from django.conf import settings
from django.contrib import admin

from wagtailtrans import models


if settings.DEBUG:
    admin.site.register(models.TranslatablePageItem)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'position', 'is_default')


class TranslatablePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'language')


admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.TranslatablePage, TranslatablePageAdmin)
