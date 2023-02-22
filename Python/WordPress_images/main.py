import seleniumBot
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

bot = seleniumBot.Bot()

# make login in website
bot.login( USERNAME, PASSWORD )

"""
bot.get_products(page) will return a dict of produts with that no image

    { "nombre" : "Name of the product" , "id" : "id of the product" }

"""
key_products = bot.get_products(page=386)
bot.find_image(nombre=key_products[0]["nombre"],path="bot/",id=key_products[0]["id"])

bot.edit_image_product(key_products[0]["id"],f'bot\{key_products[0]["id"]}.jpg',key_products[0]["nombre"])
