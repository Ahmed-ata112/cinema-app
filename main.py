import re

from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

baseUrl = "https://elcinema.com"
url = "https://elcinema.com/en/theater/1"


def write_html_to_file(html):
    with open("ht.html", "w", encoding="utf-8") as f:
        for a in html:
            f.write(str(a) + "\n")


def parse_movies_in_cinema(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    movies = soup.findAll('div', attrs={'class': 'boxed-0'})
    write_html_to_file(movies)


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

    products = []  # List to store name of the product
    prices = []  # List to store price of the product
    ratings = []  # List to store rating of the product

    print(products)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main()
    parse_movies_in_cinema("https://elcinema.com/en/theater/3101219/")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
