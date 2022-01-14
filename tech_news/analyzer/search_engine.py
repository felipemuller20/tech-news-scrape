from tech_news.database import search_news
# https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison

# Requisito 6
def search_by_title(title):
    insensitive = title.casefold()
    print (title, insensitive)
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for new in news:
        print('NEWWWWWWWWWWWWWW', (new["title"], new["url"]))
        tupla = (new["title"], new["url"])
        result.append(tupla)
    print(result)
    return result    


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
