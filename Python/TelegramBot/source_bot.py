#bot telegram


from telethon.sync import TelegramClient

#passando o token do bot para o cod:
token: str = "5929565499:AAGs4cKdfgHzSeVf3hu5PtfXo2aZE5AGnM0"

api_id = 123456
api_hash = 'YOUR_API_HASH'
phone = '+111111111111'
client = TelegramClient(phone, api_id, api_hash)

1
2
3
4
5
6
from telethon.sync import TelegramClient
api_id = 123456
api_hash = 'YOUR_API_HASH'
phone = '+111111111111'
client = TelegramClient(phone, api_id, api_hash)
 