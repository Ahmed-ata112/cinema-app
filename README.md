
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
  - `POST (Authenticated)` : Create a Movie and should be used only by the Scraper
  
`api/movies/${id}`
 - `GET` : Get a specific Movie 
 - `PUT (Authenticated)` : change the Movie object
 - `Delete (Authenticated)` : delete the Movie object





## Get deleted Thing

### Request

`GET /thing/1`

    curl -i -H 'Accept: application/json' http://localhost:7000/thing/1

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2011 12:36:33 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    {"status":404,"reason":"Not found"}

## Delete a Thing using the _method hack

### Request

`DELETE /thing/id`

    curl -i -H 'Accept: application/json' -X POST -d'_method=DELETE' http://localhost:7000/thing/2/

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 24 Feb 2011 12:36:33 GMT
    Status: 204 No Content
    Connection: close




