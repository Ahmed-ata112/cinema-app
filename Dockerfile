FROM python:latest

WORKDIR /usr/src/movie_api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py" , "runserver"]