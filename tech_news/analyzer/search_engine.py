from tech_news.database import search_news
import time

# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for new in news:
        tupla = (new["title"], new["url"])
        result.append(tupla)
    return result


# Requisito 7
def search_by_date(date):
    # https://stackoverflow.com/questions/16527878/check-if-line-is-a-timestamp-in-python
    try:
        time.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    
    news = search_news({"timestamp": {"$regex": date}})
    result = []
    for new in news:
        tupla = (new["title"], new["url"])
        result.append(tupla)
    return result


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
