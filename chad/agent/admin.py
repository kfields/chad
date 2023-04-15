from django.contrib import admin
from .models import Avatar, Bot
from .forms import AvatarAdminForm, BotAdminForm

class AvatarAdmin(admin.ModelAdmin):
    form = AvatarAdminForm

admin.site.register(Avatar, AvatarAdmin)

class BotAdmin(admin.ModelAdmin):
    form = BotAdminForm

admin.site.register(Bot, BotAdmin)