from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    title_list = search_news({'title': {'$regex': title, '$options': 'i'}})

    news = []

    for new in title_list:
        news.append((new['title'], new['url']))

    return news


# Requisito 7
def search_by_date(date):
    news = []
    try:
        string = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news_list = search_news({"timestamp": string})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        for new in news_list:
            news.append((new["title"], new["url"]))

        return news


# Requisito 8
def search_by_tag(tag):
    news = []
    tag_news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    for new in tag_news:
        news.append((new["title"], new["url"]))

    return news


# Requisito 9
def search_by_category(category):
    news = []
    category_news = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    for new in category_news:
        news.append((new["title"], new["url"]))

    return news
