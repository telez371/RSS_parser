from asyncio import sleep

import feedparser
import logging
from datetime import datetime, timezone

from sending_messages.fibery import send_fibery_message
from sending_messages.google_chat import send_message_to_google_chat, extract_thread_key_from_message_response
from sending_messages.gpt_api import get_gpt_response
from sending_messages.paeser_for_fibery import extract_budget
from sending_messages.telegram_bot import send_telegram_message
from .job_parser import format_html_for_display, prepare_text_for_gpt
from .models import RSSFeed, RSSItem, GoogleChatSettings, TelegramSettings, GPTPromptSettings, FiberyCRMSettings

logger = logging.getLogger(__name__)


class RSSHandler:
    def __init__(self):
        self.feeds = RSSFeed.objects.filter(is_enabled=True)

    def fetch_and_process_all_feeds(self):
        if not self.feeds:
            logger.info("No active RSS feeds to process.")
            return

        for rss_feed in self.feeds:
            feed = feedparser.parse(rss_feed.url)
            for entry in feed.entries:
                self.process_rss_entry(entry, rss_feed)

    def process_rss_entry(self, rss_entry, rss_feed_config):
        entry_title = rss_entry.get('title', 'No title')
        entry_link = rss_entry.get('link', 'No link')
        entry_published_date = rss_entry.get('published', 'No publication date')
        entry_description_html = rss_entry.get('description', '')
        formatted_description = format_html_for_display(entry_title, entry_description_html, entry_link)

        entry_guid = rss_entry.get('guid', rss_entry.get('link'))
        parsed_published_date = self.parse_date(entry_published_date)

        if parsed_published_date.date() == datetime.now(timezone.utc).date():
            if not RSSItem.objects.filter(guid=entry_guid).exists():
                new_rss_item = RSSItem(title=entry_title, guid=entry_guid)
                new_rss_item.save()

                google_chat_config = GoogleChatSettings.objects.filter(rss_feed=rss_feed_config).first()
                gpt_prompt_config = GPTPromptSettings.objects.filter(rss_feed=rss_feed_config).first()
                fibery_config = FiberyCRMSettings.objects.filter(rss_feed=rss_feed_config).first()
                telegram_config = TelegramSettings.objects.filter(rss_feed=rss_feed_config).first()

                if google_chat_config.is_enabled:
                    chat_response = send_message_to_google_chat(google_chat_config, formatted_description)
                    chat_thread_key = extract_thread_key_from_message_response(chat_response)

                    if gpt_prompt_config.is_enabled:
                        gpt_input_text = prepare_text_for_gpt(entry_description_html)
                        gpt_generated_response = get_gpt_response(gpt_input_text, gpt_prompt_config)
                        send_message_to_google_chat(google_chat_config, gpt_generated_response, chat_thread_key)

                if telegram_config.is_enabled:
                    if telegram_config:
                        send_telegram_message(telegram_config, formatted_description)

                if fibery_config.is_enabled:
                    price = extract_budget(formatted_description)
                    send_fibery_message(entry_title, price, formatted_description, fibery_config)

    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
        except ValueError:
            logger.error(f"Error parsing date: {date_str}")
            return datetime.now(timezone.utc)


