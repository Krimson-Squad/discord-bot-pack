from discord_webhook import DiscordWebhook
from modules.jokes import *
webhook_url="<your webhook url>"
webhook = DiscordWebhook(url=webhook_url, content=msg)
response = webhook.execute()
