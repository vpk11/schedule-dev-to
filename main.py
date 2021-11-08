from services.dev_to_service import DevToService
import utils.constants as constants

def main():
    for tag in constants.tags:
        DevToService().publish_top_article_to_telegram(tag)

if __name__ == "__main__":
    main()
