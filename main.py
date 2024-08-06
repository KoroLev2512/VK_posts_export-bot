import requests


class TelegramApi:
    def __init__(self, token):
        self.base_url = f"https://api.telegram.org/bot{token}"

    def set_webhook(self, url):
        method_name = self.base_url + "/setWebhook"
        json = {"url": url}
        response = requests.post(method_name, json=json)
        print(response.text)


if __name__ == "__main__":
    tg_bot = TelegramApi("7468754032:AAGn_xvms7WJoFdOXZBDbBo1M7sY27AxwDo")
    tg_bot.set_webhook("https://d100-83-239-63-182.ngrok-free.app/tg_hook")
