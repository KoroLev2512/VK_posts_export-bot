import requests


class TelegramApi:
    def __init__(self, token):
        self.base_url = f"https://api.telegram.org/bot{token}"

    def set_webhook(self, url):
        method_name = self.base_url + "/setWebhook"
        json = {"url": url}
        response = requests.post(method_name, json=json)
        print(response.text)

    def send_message(self, chat_id, text):
        method_name = self.base_url + "/sendMessage"
        json = {"chat_id": chat_id, "text": text}
        response = requests.post(method_name, json=json)
        print(response.text)

    def send_document(self, chat_id, document):
        method_name = self.base_url + "/sendDocument"
        json = {"chat_id": chat_id, "document": document}
        response = requests.post(method_name, json=json)
        print(response.text)
