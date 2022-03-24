import requests
from bs4 import BeautifulSoup
import random
import threading

CRUNCHHYPE_URL = "https://www.crunchhype.com/"
WIRED_URL = "https://www.wired.com/feed/google-latest-news/sitemap-google-news"
NYTIMES_URL = "https://www.nytimes.com/sitemaps/new/news-1.xml.gz"
THEVERGE_URL = "https://www.theverge.com/sitemaps/google_news"
NEWS = dict()


def news() -> dict:
    crunchhype_thread = threading.Thread(target=crunchhype_news())
    wired_thread = threading.Thread(target=wired_news())
    nytimes_thread = threading.Thread(target=nytimes_news())
    theverge_thread = threading.Thread(target=theverge_news())
    crunchhype_thread.run()
    wired_thread.run()
    nytimes_thread.run()
    theverge_thread.run()
    return NEWS


def crunchhype_news() -> None:
    Soup = BeautifulSoup(requests.get(CRUNCHHYPE_URL).text, 'lxml')
    links = Soup.find_all(class_="entry-title-link")
    crunchhype_result = [(link["href"], link["title"]) for link in links]
    random.shuffle(crunchhype_result)
    NEWS["www.crunchhype.com"] = crunchhype_result


def wired_news() -> None:
    Soup = BeautifulSoup(requests.get(WIRED_URL).text, 'lxml')
    links = [link.text for link in Soup.findAll("loc")]
    titles = [title.text for title in Soup.findAll("news:title")]
    wired_result = [(link, title) for link, title in zip(links, titles)]
    random.shuffle(wired_result)
    NEWS["www.wired.com"] = wired_result


def nytimes_news() -> None:
    Soup = BeautifulSoup(requests.get(NYTIMES_URL).text, 'lxml')
    links = [link.text for link in Soup.findAll("loc")]
    titles = [title.text for title in Soup.findAll("news:title")]
    nytimes_result = [(link, title) for link, title in zip(links, titles)]
    random.shuffle(nytimes_result)
    NEWS["www.nytimes.com"] = nytimes_result


def theverge_news() -> None:
    Soup = BeautifulSoup(requests.get(THEVERGE_URL).text, 'lxml')
    links = [link.text for link in Soup.findAll("loc")][0:6]
    titles = [title.text for title in Soup.findAll("news:title")]
    theverge_result = [(link, title) for link, title in zip(links, titles)]
    random.shuffle(theverge_result)
    NEWS["www.theverge.com"] = theverge_result
