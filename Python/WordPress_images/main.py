import seleniumBot
import os
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

bot = seleniumBot.Bot()
bot.login( USERNAME, PASSWORD )
a = bot.get_products(386)
bot.edit_image_product(a[0])