from django.contrib import admin
from .models import RSSFeed, GoogleChatSettings, TelegramSettings, GPTPromptSettings, FiberyCRMSettings
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    login_template = 'admin/login.html'


admin_site = MyAdminSite(name='myadmin')


@admin.register(RSSFeed)
class RSSFeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_filter = ('is_enabled',)
    search_fields = ('name',)



@admin.register(GoogleChatSettings)
class GoogleChatSettingsAdmin(admin.ModelAdmin):
    list_display = ('chat_name', 'webhook_url', 'is_enabled')
    list_filter = ('is_enabled',)
    search_fields = ('name',)


@admin.register(TelegramSettings)
class TelegramSettingsAdmin(admin.ModelAdmin):
    list_display = ('api_key', 'chat_id', 'is_enabled')
    list_filter = ('is_enabled',)
    search_fields = ('chat_id',)


@admin.register(GPTPromptSettings)
class GPTPromptSettingsAdmin(admin.ModelAdmin):
    list_display = ('prompt_name', 'prompt_text', 'is_enabled')
    list_filter = ('is_enabled',)
    search_fields = ('name',)


@admin.register(FiberyCRMSettings)
class FiberyCRMSettingsAdmin(admin.ModelAdmin):
    list_display = ('fibery_url', 'is_enabled')
    list_filter = ('is_enabled',)
