import requests
import time
from parsel import Selector


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
    parsel_selector = Selector(text=html_content)
    url = parsel_selector.css("a.cs-overlay-link::attr(href)").getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    next_page = (
        Selector(html_content).css("a.next.page-numbers::attr(href)").get()
    )
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
