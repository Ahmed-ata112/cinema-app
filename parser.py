
from unicodedata import name
from bs4 import BeautifulSoup, Tag
from urllib.request import urlopen
from django.core.exceptions import ObjectDoesNotExist
from movies_api.models import *
import requests

TOKEN = "token 806045a676ffb81d29f90fbacc788558a99a6b4a"

# Cinema
# Movie
# All Cinames
# All Movies


class MovieStruct:
    movie_title = ''
    movie_image = ''
    movie_description = ''
    movie_genre = ''
    movie_link_id = ''
    movie_rating = 0.0
    cinema = 0

    def save(self):
        # return requests.post('http://localhost:8000/api/movies/',
        #  data=self.to_json(), headers={'Authorization': TOKEN})

        try:
            retrieved = MovieItem.objects.get(movie_title=self.movie_title)
            retrieved.cinema.add(self.cinema)
            retrieved.save()
        except ObjectDoesNotExist:
            retrieved = MovieItem(movie_title=self.movie_title,
                                  movie_image=self.movie_image,
                                  movie_description=self.movie_description,
                                  movie_genre=self.movie_genre,
                                  movie_link_id=self.movie_link_id,
                                  movie_rating=self.movie_rating,
                                  )
            retrieved.save()
            retrieved.cinema.add(self.cinema)

    def to_json(self):
        return {
            'movie_title': self.movie_title,

            'movie_image': self.movie_image,
            'movie_description': self.movie_description,
            'movie_genre': self.movie_genre,
            'movie_link_id': self.movie_link_id,
            'movie_rating': self.movie_rating,
        }


class CinemaStruct:
    cinema_name = ''
    cinema_link = ''

    # def save(self):
    # return requests.post('http://localhost:8000/api/cinemas/',
    #  data=self.to_json(), headers={'Authorization': TOKEN})

    # convert to json

    def to_json(self):
        return {
            'cinema_name': self.cinema_name,
            'cinema_link': self.cinema_link,
        }

    def __str__(self):
        return self.cinema_name


def write_html_to_file(html):
    with open("ht.html", "w", encoding="utf-8") as f:
        for a in html:
            f.write(str(a) + "\n")


class Parser():
    def __init__(self):
        self.theaterBaseUrl = "https://elcinema.com/en/theater/"
        self.baseUrl = "https://elcinema.com"
        self.curr_movie = MovieStruct()
        self.curr_cinema = CinemaStruct()

    def parse_movie_details(self, url):
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        def filter_details(tag):
            return tag.has_attr("href") and tag['href'].startswith("/en/index/work/genre/")

        genre = soup.find(filter_details)
        print(f"genre  {genre.text}")
        self.curr_movie.movie_genre = genre.text
        descriptions = soup.find(
            'div', attrs={'class': 'columns small-12 medium-9 large-9'})

        res = descriptions.findAll('p')
        print(f"description: {res[0].text}")
        self.curr_movie.movie_description = res[0].text
        rating = soup.find('div', attrs={'class': 'stars-orange-60'}).text

        print(rating)
        self.curr_movie.movie_rating = float(rating)
        self.curr_movie.save()

    def parse_movies_in_cinema(self, url):
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        def filter_movies(tag):
            return (not tag.has_attr("class")) and tag.has_attr("href") and tag['href'].startswith("/en/work/")

        movies = soup.findAll(filter_movies)

        i = 0
        while i < len(movies):
            print("image is " + movies[i].find('img')['data-src'])
            self.curr_movie.movie_image = movies[i].find('img')['data-src']
            i += 1
            print("title is " + movies[i].text)
            self.curr_movie.movie_title = movies[i].text
            self.curr_movie.movie_link_id = movies[i]['href']

            movie_link = self.baseUrl + movies[i]['href']
            print("link + " + movie_link)
            self.parse_movie_details(movie_link)
            i += 1

    def parse_cinames(self):
        for i in range(1, 11):
            page = urlopen(self.theaterBaseUrl + str(i))
            print(self.theaterBaseUrl + str(i))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            cinemas = soup.findAll(
                'div', attrs={'class': 'jumbo-theater clearfix'})
            # write_html_to_file(cinemas)

            def cinn_filter(tag):
                return tag.has_attr("href") and tag['href'].startswith("/en/theater/")

            for cinema in cinemas:
                try:
                    curr_cinema = cinema.find(cinn_filter)
                    print(curr_cinema.text.strip())
                    print(self.baseUrl + curr_cinema['href'])
                    c = CinemaItem(cinema_name=curr_cinema.text.strip(),
                                   cinema_link=(self.baseUrl + curr_cinema['href']))
                    c.save()
                    # self.curr_cinema.cinema_name = curr_cinema.text.strip()
                    # self.curr_cinema.cinema_link = self.baseUrl + \
                    # curr_cinema['href']
                    self.curr_movie.cinema = c

                    self.parse_movies_in_cinema(
                        self.baseUrl + curr_cinema['href'])
                    print('='*50)
                except Exception as e:
                    print(e)

    def init(self):
        self.parse_cinames()
