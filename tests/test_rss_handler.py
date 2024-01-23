from django.test import TestCase
from unittest.mock import patch, MagicMock
from rss_handler.models import RSSFeed
from rss_handler.rss_handler import RSSHandler


class RSSHandlerTest(TestCase):
    def setUp(self):
        RSSFeed.objects.create(url='http://example.com/rss')
        RSSFeed.objects.create(url='http://example2.com/rss')

    @patch('rss_handler.rss_handler.feedparser.parse')
    def test_fetch_and_process_all_feeds(self, mock_parse):
        mock_entry = {
            'title': 'Test Entry',
            'link': 'http://example.com/1',
            'published': 'Today',
            'description': '<p>Description</p>'
        }

        mock_parse.return_value = MagicMock(entries=[mock_entry, mock_entry])

        handler = RSSHandler()
        handler.fetch_and_process_all_feeds()

        self.assertEqual(mock_parse.call_count, 2)

