from django.db import models


class RSSFeed(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True, max_length=2000)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class GPTPromptSettings(models.Model):
    rss_feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)
    prompt_name = models.CharField(max_length=200)
    prompt_text = models.TextField()
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.prompt_name


class GoogleChatSettings(models.Model):
    rss_feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)
    chat_name = models.CharField(max_length=200)
    webhook_url = models.URLField(max_length=2000)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.chat_name


class TelegramSettings(models.Model):
    rss_feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=200)
    chat_id = models.CharField(max_length=200)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.rss_feed.name


class FiberyCRMSettings(models.Model):
    rss_feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)
    fibery_url = models.URLField(max_length=2000)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.rss_feed.name


class RSSItem(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    guid = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.title or "No Title"
