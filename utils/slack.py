from django.conf import settings

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def slack_send(text):
    client = WebClient(token=settings.SLACK_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=settings.SLACK_CHANNEL,
            text=text
        )
        print(f"Mensaje enviado: {response['message']['text']}")
    except SlackApiError as e:
        print(f"Error al enviar el mensaje: {e.response['error']}")
    return True

