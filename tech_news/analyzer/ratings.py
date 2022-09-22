from tech_news.database import find_news


# Requisito 10
def top_5_news():
    result = find_news()
    sorted_news = sorted(
        result, key=lambda data: data["comments_count"], reverse=True
    )[:5]
    news = []

    for new in sorted_news:
        news.append((new["title"], new["url"]))

    return news


# Requisito 11
def top_5_categories():
    result = find_news()
    categories = dict()
    news = []

    for new in result:
        if new['category'] in categories:
            categories[new['category']] += 1
        else:
            categories[new["category"]] = 0

    sorted_categories = sorted(
        categories.items(), key=lambda x: (-x[1], x[0]))

    for new in sorted_categories:
        news.append(new[0])

    return news
