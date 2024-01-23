from json import dumps

from django.test import TestCase
from unittest.mock import patch

from django.conf import settings
from sending_messages.google_chat import send_message_to_google_chat


class SendMessageToGoogleChatTests(TestCase):

    @patch('er.google_chat.Http')
    def test_send_message_to_google_chat(self, mock_http):
        mock_http().request.return_value = ({"status": "200"}, b'{}')

        send_message_to_google_chat("Test message")

        mock_http().request.assert_called_once_with(
            uri=settings.GOOGLE_CHAT_WEBHOOK_URL,
            method="POST",
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=dumps(
                {
                    "text": "Test message",
                    "thread": {
                        "threadKey": "THREAD_KEY_VALUE"
                    }
                }
            ),
        )
