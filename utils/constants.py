import os
from dotenv import load_dotenv

load_dotenv()

base_url = 'https://dev.to'
articles_url = base_url + '/api/articles?tag={0}&top={1}&state={2}&page={3}&per_page={4}'
tags = ['ruby', 'rails', 'python', 'javascript']
top = 10
state = 'fresh'
page = 1
per_page = 1
bot_url = os.environ['BOT_URL']
telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
parse_mode="Markdown"
