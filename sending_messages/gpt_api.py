import openai
from django.conf import settings

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)


def get_gpt_response(user_message, prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": prompt.prompt_text},
                {"role": "user", "content": user_message},
            ]
        )

        return response.choices[0].message.content
    except Exception:
        return ("If you see this message,"
                " it is possible that the balance has run out or an error occurred."
                " Please check the OpenAI dashboard and the error message: ")
