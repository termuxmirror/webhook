# webhook.py

import requests

class Webhook:
    def __init__(self, url):
        self.url = url

    def send_webhook(self, message):
        data = {"content": message}
        response = requests.post(self.url, json=data)
        if response.status_code == 200:
            print("Webhook sent successfully.")
        else:
            print(f"Failed to send webhook. Status code: {response.status_code}")
        return response  # Rückgabe der Antwort

# Beispiel für die Verwendung:
# webhook = Webhook('webhook_url')
# response = webhook.send_webhook('Testnachricht')
# print("Response:", response.text)
