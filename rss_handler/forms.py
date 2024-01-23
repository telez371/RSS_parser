from django import forms
from .models import RSSFeed, GPTPromptSettings, GoogleChatSettings, TelegramSettings, FiberyCRMSettings


class RSSFeedForm(forms.ModelForm):
    class Meta:
        model = RSSFeed
        fields = ['name', 'url', 'is_enabled']


class GPTPromptSettingsForm(forms.ModelForm):
    class Meta:
        model = GPTPromptSettings
        fields = ['rss_feed', 'prompt_name', 'prompt_text', 'is_enabled']


class GoogleChatSettingsForm(forms.ModelForm):
    class Meta:
        model = GoogleChatSettings
        fields = ['rss_feed', 'chat_name', 'webhook_url', 'is_enabled']


class TelegramSettingsForm(forms.ModelForm):
    class Meta:
        model = TelegramSettings
        fields = ['rss_feed', 'api_key', 'chat_id', 'is_enabled']


class FiberyCRMSettingsForm(forms.ModelForm):
    class Meta:
        model = FiberyCRMSettings
        fields = ['rss_feed', 'fibery_url', 'is_enabled']
