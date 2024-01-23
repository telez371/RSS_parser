from django.core.management.base import BaseCommand
from rss_handler.rss_handler import RSSHandler


class Command(BaseCommand):
    help = 'Fetch and process RSS feeds'

    def handle(self, *args, **kwargs):
        handler = RSSHandler()
        handler.fetch_and_process_all_feeds()
