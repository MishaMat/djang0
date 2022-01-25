from django.contrib import admin
from forms6.models import *


# Register your models here.

@admin.register(NewsModel)
class NewsModelsAdmin(admin.ModelAdmin):
    pass


@admin.register(FlagModel)
class FlagModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    pass
