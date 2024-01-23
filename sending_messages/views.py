# from rss_handler.rss_handler import logger
# from .google_chat import send_message_to_google_chat
# from .gpt_api import get_gpt_response
#
#
# def process_and_send_prompt(google_chat_settings, gpt_prompt_settings, prompt_text, thread_key=None):
#     try:
#         if google_chat_settings.is_enabled:
#             if not thread_key:
#                 response_data = send_message_to_google_chat(google_chat_settings, prompt_text)
#                 thread_key = extract_thread_key_from_message_response(response_data)
#
#             if thread_key and gpt_prompt_settings.is_enabled:
#                 gpt_response = get_gpt_response(prompt_text, gpt_prompt_settings)
#                 send_message_to_google_chat(google_chat_settings, gpt_response, thread_key)
#             else:
#                 logger.error("Failed to send the initial message to Google Chat or retrieve the thread key.")
#         else:
#             logger.error("Google Chat settings are not enabled or not found.")
#     except Exception as e:
#         logger.error(f"An error occurred in process_and_send_prompt: {e}")
#
#
# def extract_thread_key_from_message_response(response_data):
#     print("Response received:", response_data)
#
#     thread_name = response_data.get('thread', {}).get('name', '')
#     if thread_name:
#         parts = thread_name.split('/')
#         if len(parts) > 0:
#             print("Extracted thread key:", parts[-1])
#             return parts[-1]
#     else:
#         print("No thread info in response")
#     return None