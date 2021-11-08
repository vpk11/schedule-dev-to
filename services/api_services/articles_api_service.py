import requests
from services.api_services.base import Base
from utils.helper_methods import response_parser
import utils.constants as constants

class ArticlesApiService(Base):
    def __init__(self):
        print('ArticlesApiService')

    def fetch(self, tag):
        try:
            url = constants.articles_url.format(
                tag, constants.top, constants.state, constants.page,
                constants.per_page
            )
            response = requests.get(url)
            json_data = response.json()
            print(f"Json data:articles -> {json_data}")
            return response_parser(json_data)
        except Exception as e:
            print(f"Exception: {e}")
            return self.handle_error(e)