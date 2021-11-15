import requests
from bs4 import BeautifulSoup

iamhuman = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.118 Whale/2.11.126.23 Safari/537.36"
}

def taling_crawling(keyword: str) -> list:
    URL = f"https://taling.me/Home/Search/?query={keyword}"

    result = requests.get(URL, headers=iamhuman)
    soup = BeautifulSoup(result.text, "html.parser")

    lecture = soup.find('div', {"class": "cont2"})

    # title
    title = lecture.find_all("div", {"class": "title"})
    titles = []
    for i in title:
        titles.append(i.text.strip())

    # profile
    profile = lecture.find_all("div", {"class": "name"})
    profiles = []
    for i in profile:
        profiles.append(i.text.strip())

    # price
    price = lecture.find_all("div", {"class", "price2"})
    prices = []
    for i in price:
        prices.append(i.text.strip())

    # location
    location = lecture.find_all("div", {"class": "location"})
    locations = []
    for i in location:
        locations.append(i.text.strip())

    # link
    link = lecture.find_all("a")
    links = []
    for i in link:
        href = f"https://taling.me{i.attrs['href']}"
        links.append(href)

    lecture_list = list(zip(titles, profiles, prices, locations, links))
    return lecture_list