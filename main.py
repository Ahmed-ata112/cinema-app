import re

from bs4 import BeautifulSoup, Tag
import pandas as pd
from urllib.request import urlopen

baseUrl = "https://elcinema.com"
url = "https://elcinema.com/en/theater/1"


def write_html_to_file(html):
    with open("ht.html", "w", encoding="utf-8") as f:
        for a in html:
            f.write(str(a) + "\n")


def filter_movies(tag):
    return not tag.has_attr("class")


def parse_movies_in_cinema(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    movies = soup.findAll(filter_movies, href=re.compile('/en/work/*'))
    write_html_to_file(movies)
    i = 0
    while i < len(movies):
        print("image is " + movies[i].find('img')['data-src'])
        i += 1
        print("title is " + movies[i].text)
        print("link + " + baseUrl + movies[i]['href'])
        i += 1


def main():
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    cinemas = soup.findAll('div', attrs={'class': 'jumbo-theater clearfix'})
    # write_html_to_file(cinemas)
    for cinema in cinemas:
        curr_cinema = cinema.find(href=re.compile('/en/theater/*'))
        print(curr_cinema.text.strip())
        print(baseUrl + curr_cinema['href'])
        parse_movies_in_cinema(baseUrl + curr_cinema['href'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
