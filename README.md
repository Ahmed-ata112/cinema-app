
# Cinema  App

A Project that Scrapes All the movies and cinemas all over Egypt and other Countries in The MENA, Providing them as a RESTful API


## API Reference
#### Get all Cinemas
```http
  GET /api/cinemas
```
#### Get Cinema
```http
  GET /api/cinemas/${id}
```
#### Get all Movies
```http
  GET /api/movies
```
#### Get Movie
```http
  GET /api/movies/${id}
```

|====================================

## Install requirements

    pip install -r requirements.tct

## Run the app

    python manage.py runserver

## Run the Scraper Manually
The scraper runs daily automatically but can be run thru

    python manage.py runparser

# REST API

The REST API to the example app is described below.

## Get list of Cinemas

### Request

`api/cinemas/`
  - `GET` : Get all cinemas
  - `POST (Authenticated)` : Create a Cinema and should be used only by the Scraper
  
`api/cinemas/${id}`
 - `GET` : Get a specific Cinema 
 - `PUT (Authenticated)` : change the Cinema object
 - `Delete (Authenticated)` : delete the Cinema object

`api/movies/`
  - `GET` : Get all movies
  
  It can be filtered with `movie_title` , `movie_genres` and `movie_rating`

  #### example

    It can be filtered with `movie_title` , `movie_genres` and `movie_rating`

  - `POST (Authenticated)` : Create a Movie and should be used only by the Scraper
  
    

`api/movies/${id}`
 - `GET` : Get a specific Movie 
 - `PUT (Authenticated)` : change the Movie object
 - `Delete (Authenticated)` : delete the Movie object

`api/genres/`
  - `GET` : Get all genres of the movies
  




