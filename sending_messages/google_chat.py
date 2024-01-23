import json
from json import dumps
from httplib2 import Http


def send_message_to_google_chat(google_chat_settings, message_text, thread_key=None):
    app_message = {"text": message_text}

    if thread_key:
        app_message["thread"] = {"name": thread_key}
        new_thread = '&messageReplyOption=REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD'
        google_chat_settings.webhook_url = google_chat_settings.webhook_url + new_thread

    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response, content = http_obj.request(
        uri=google_chat_settings.webhook_url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )

    if response.status == 200:
        response_data = json.loads(content.decode('utf-8'))

        return response_data
    else:
        return None


def extract_thread_key_from_message_response(response_data):
    try:
        if 'thread' in response_data:
            thread_key = response_data['thread']['name']
            return thread_key
        return None
    except Exception:
        return None