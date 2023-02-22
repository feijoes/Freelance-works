import seleniumBot
import os
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

bot = seleniumBot.Bot()
bot.login( USERNAME, PASSWORD )
bot.get_products(386)