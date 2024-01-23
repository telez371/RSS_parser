from unittest import TestCase
from unittest.mock import patch

from sales_app import settings
from sending_messages.telegram_bot import send_telegram_message


class TestTelegramBot(TestCase):

    @patch('er.telegram_bot.bot')
    def test_send_telegram_message(self, mock_bot):
        test_chat_id = settings.TELEGRAM_CHAT_ID

        mock_bot.send_message.return_value = None

        send_telegram_message("Тестовое сообщение")

        mock_bot.send_message.assert_called_once_with(test_chat_id, "Тестовое сообщение")
