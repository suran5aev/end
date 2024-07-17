from django.contrib import admin
from apps.base.models import Base, Our_advantages, Popular_category, Our_chef, News, Menu, Dessert, Sea_Food, BEVERAGE
from modeltranslation.admin import TranslationAdmin
from typing import Any
from django.http import HttpRequest

# Register your models here.

admin.site.register(Base)
admin.site.register(Popular_category)
admin.site.register(Our_chef)
admin.site.register(News)
admin.site.register(Menu)
admin.site.register(Dessert)
admin.site.register(Sea_Food)
admin.site.register(BEVERAGE)



class Our_advantagesTranslationAdmin(TranslationAdmin):
    model = Our_advantages
    
    def get_fieldsets(self, request: HttpRequest, obj: Any = None):
        fieldsets = (
            ('Русская версия', {
                'fields': ('title_ru', 'description_ru'),
            }),
            ('Кыргызская версия', {
                'fields': ('title_ky', 'description_ky'),
            }),
        )
        return fieldsets


admin.site.register(Our_advantages, Our_advantagesTranslationAdmin)



