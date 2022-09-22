import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"User-Agent": "Fake user-agent"}
        )
        response.raise_for_status()
        time.sleep(1)
        return response.text

    except requests.Timeout:
        return None

    except requests.exceptions.HTTPError:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url = selector.css("a.cs-overlay-link::attr(href)").getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    next_page = (
        Selector(html_content).css("a.next.page-numbers::attr(href)").get()
    )
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    return {
        "url": selector.css("link[rel=canonical] ::attr(href)").get(),
        "title": selector.css("h1.entry-title ::text").get().strip(),
        "timestamp": selector.css("li.meta-date ::text").get(),
        "writer": selector.css("span.author > a.url::text").get(),
        "comments_count": len(selector.css("div.comment-body").getall()),
        "summary": "".join(selector.css(
            ".entry-content > p:nth-of-type(1) ::text").getall()).strip(),
        "tags": selector.css(
            "section.post-tags > ul > li > a ::text").getall(),
        "category": selector.css("a.category-style > span.label ::text").get()
    }


# Requisito 5
def get_tech_news(amount):
    list_news = []
    url = "https://blog.betrybe.com/"
    response = fetch(url)
    next_page_link = scrape_next_page_link(response)
    news = scrape_novidades(response)

    while len(news) < amount:
        next_page = fetch(next_page_link)
        next_news = scrape_novidades(next_page)
        news += next_news
        next_page_link = scrape_next_page_link(next_page)

    for index in range(0, amount):
        news_link = fetch(news[index])
        news_scraped = scrape_noticia(news_link)
        list_news.append(news_scraped)

    create_news(list_news)
    return list_news
