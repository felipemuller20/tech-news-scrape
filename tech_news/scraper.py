import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if response.status_code != 200:
        return None

    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news_list = []
    for news in selector.css("h3.tec--card__title a::attr(href)").getall():
        news_list.append(news)

    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.tec--btn::attr(href)").get()

    if next_page:
        return next_page
    return None


# Requisito 4

def get_url(selector):
    current_url = selector.css("head link[rel=canonical]::attr(href)").get()
    return current_url


def get_title(selector):
    title = selector.css("h1#js-article-title::text").get()
    return title


def get_date(selector):
    date = selector.css("time#js-article-date::attr(datetime)").get()
    return date


def get_author(selector):
    # name = selector.css("a.tec--author__info__link::text").get()
    # return name.strip() if name else None
    name = selector.css("a.tec--author__info__link::text").get()
    if name:
        return name.strip()
    otherName = selector.css("div.tec--timestamp__item a::text").get()
    if otherName:
        return otherName.strip()
    oneMore = selector.css(
        "div.tec--author__info > p:first_child *::text").get()
    if oneMore:
        return oneMore.strip()

    return None


def get_share(selector):
    shares = selector.css("div.tec--toolbar__item::text").get()
    return int(shares.split()[0]) if shares else 0


def get_comments(selector):
    comments = selector.css("button#js-comments-btn::attr(data-count)").get()
    return int(comments)


def get_first_paragraph(selector):
    paragraph = selector.css(
        ".tec--article__body > p:first_child *::text").getall()
    return "".join(paragraph)


def get_sources(selector):
    sources = selector.css("div.z--mb-16 a::text").getall()
    all_sources = []
    for source in sources:
        all_sources.append(source.strip())
    return all_sources


def get_categories(selector):
    categories = selector.css("#js-categories a::text").getall()
    all_categories = []
    for categorie in categories:
        all_categories.append(categorie.strip())
    return all_categories


def scrape_noticia(html_content):
    selector = Selector(html_content)
    return {
        "url": get_url(selector),
        "title": get_title(selector),
        "timestamp": get_date(selector),
        "writer": get_author(selector),
        "shares_count": get_share(selector),
        "comments_count": get_comments(selector),
        "summary": get_first_paragraph(selector),
        "sources": get_sources(selector),
        "categories": get_categories(selector)
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
