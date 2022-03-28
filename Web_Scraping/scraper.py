import requests
from bs4 import BeautifulSoup
import random
import threading
from difflib import SequenceMatcher
# Some links for scraping the news.
CRUNCHHYPE_URL = "https://www.crunchhype.com/"
WIRED_URL = "https://www.wired.com/feed/google-latest-news/sitemap-google-news"
NYTIMES_URL = "https://www.nytimes.com/sitemaps/new/news-1.xml.gz"
THEVERGE_URL = "https://www.theverge.com/sitemaps/google_news"
# List variable for storing results.
NEWS = list()

def news() -> list:
    """ This the main function which uses all the below functions to get news data using muti-threading.

    Returns:
        dict: return the result in dictionary format, where the link of the website is the key.
                Each key contains a nested list, which contains the title and link of the news.
    """
    crunchhype_thread = threading.Thread(target=crunchhype_news())
    wired_thread = threading.Thread(target=wired_news())
    nytimes_thread = threading.Thread(target=nytimes_news())
    theverge_thread = threading.Thread(target=theverge_news())
    crunchhype_thread.run()
    wired_thread.run()
    nytimes_thread.run()
    theverge_thread.run()
    global NEWS
    NEWS = NEWS[0:100]
    filtered_data = deduplication_validate(NEWS)
    random.shuffle(filtered_data)
    return filtered_data


def crunchhype_news() -> None:
    """ Web scraping news from crunchhype website.
    """
    Soup = BeautifulSoup(requests.get(CRUNCHHYPE_URL).text, 'lxml')
    links = Soup.find_all(class_="entry-title-link")
    for link in links:
        NEWS.append([link["href"], link["title"],"www.crunchhype.com"])
    random.shuffle(NEWS)

def wired_news() -> None:
    """ Web scraping news from wired website.
    """
    Soup = BeautifulSoup(requests.get(WIRED_URL).text, 'lxml')
    links = [link.text for link in Soup.findAll("loc")]
    titles = [title.text for title in Soup.findAll("news:title")]
    for link, title in zip(links, titles):
        NEWS.append([link, title,"www.wired.com"])
    random.shuffle(NEWS)

def nytimes_news() -> None:
    """ Web scraping news from nytimes website.
    """
    Soup = BeautifulSoup(requests.get(NYTIMES_URL).text, 'lxml')
    links = [link.text for link in Soup.findAll("loc")]
    titles = [title.text for title in Soup.findAll("news:title")]
    for link, title in zip(links, titles):
        NEWS.append([link, title,"www.nytimes.com"])
    random.shuffle(NEWS)

def theverge_news() -> None:
    """ Web scraping news from theverge website.
    """
    Soup = BeautifulSoup(requests.get(THEVERGE_URL).text, 'lxml')
    links = [link.text for link in Soup.findAll("loc")]
    titles = [title.text for title in Soup.findAll("news:title")]
    for link, title in zip(links, titles):
        NEWS.append([link, title,"www.theverge.com"])
    random.shuffle(NEWS)

def deduplication_validate(unfiltered_data: list) -> list:
    _ratio, resultant_list = 0, []
    length = len(unfiltered_data)
    for i in range(length-1):
        for j in range(i + 1, length):
            _ratio = SequenceMatcher(None, unfiltered_data[i][1], unfiltered_data[j][1]).ratio()
            if _ratio < 0.8:
                resultant_list.append(unfiltered_data[i])
    return remove_duplicates(resultant_list)

def remove_duplicates(unfiltered_data) -> list:
    new_data = []
    for data in unfiltered_data:
        if data not in new_data:
            new_data.append(data)
    return new_data
