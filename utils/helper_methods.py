from models.article import Article

def response_parser(response):
    article = None
    if not response: return { 'article': article }

    for a in response:
        article = Article(
            type_of=a.get('type_of'),
            id=a.get('id'),
            title=a.get('title'),
            description=a.get('description'),
            readable_publish_date=a.get('readable_publish_date'),
            url=a.get('url'),
            published_timestamp=a.get('published_timestamp'),
            created_at=a.get('created_at'),
            published_at=a.get('published_at'),
            reading_time_minutes=a.get('reading_time_minutes'),
        )
    return { 'article': article, 'error': None }

def resolve_articles_tg_messages(data):
    message = None
    if data.get('error'):
        return message

    article = data.get('article')
    message = "*{0}*\n{1}\n{2}".format(
        article.title, article.description, article.url
    )

    return message