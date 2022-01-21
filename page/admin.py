from django.contrib import admin
from page.models import *


# Register your models here.

@admin.register(AdvStatus)
class AdvStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    pass
