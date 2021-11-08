from services.telegram_service import TelegramSerivce as Telegram
from services.api_services.articles_api_service import ArticlesApiService
from utils.helper_methods import resolve_articles_tg_messages
import utils.constants as constants

class DevToService(object):
    def publish_top_article_to_telegram(self, tag):
        articles_api_service = ArticlesApiService()
        data = articles_api_service.fetch(tag)
        telegram = Telegram()
        message = resolve_articles_tg_messages(data)
        telegram.publish(message)
        return True
