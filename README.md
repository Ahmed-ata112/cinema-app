
# Cinema App

A Project that Scrapes the movies and cinemas all over Egypt and other Countries in The MENA, Providing them as a RESTful API using Django REST framework


## Install requirements

    pip install -r requirements.txt

## Run the app

    python manage.py runserver

## Run the Scraper Manually
The scraper runs daily automatically but you can run it manually

    python manage.py runparser


## API Reference

- ###  api/cinemas/
  - `GET` : Get all cinemas
  - `POST (Authenticated)` : Create a Cinema and should be used only by the Scraper
  
- ### api/cinemas/${id}
   - `GET` : Get a specific Cinema 
   - `PUT (Authenticated)` : change the Cinema object
   - `Delete (Authenticated)` : delete the Cinema object

- ### api/movies/
    - `GET` : Get all movies
  
      It can be filtered with `movie_title` , `movie_genres` and `movie_rating`


      #### example:

          curl http://localhost:8000/api/movies/?movie_title=Avatar&movie_genres=Animation&movie_rating=&order=-rating

  - `POST (Authenticated)` : Create a Movie and should be used only by the Scraper
  

- ### api/movies/${id}
  - `GET` : Get a specific Movie 
  - `PUT (Authenticated)` : change the Movie object
  - `Delete (Authenticated)` : delete the Movie object

- ### `api/genres/`
    - `GET` : Get all genres of the movies
  
## Docker
The server can run with 

    docker compose up


