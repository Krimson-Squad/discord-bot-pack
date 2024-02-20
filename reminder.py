import argparse
from discord_webhook import DiscordWebhook
webhook_url="<your webhook url"
def main():
    parser = argparse.ArgumentParser(description="Reminder Bot for NepTech Tribe Discord Server")
    parser.add_argument("-m", "--message", type=str, help="message")
    args = parser.parse_args()
    
    message = args.message
    
    if message:
        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()
    else:
        print("No message provided.")

if __name__ == "__main__":
    main()
