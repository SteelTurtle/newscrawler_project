# newscrawler_project
A super simple newsfeed with support for ReST, made with django 1.11

NewsCrawler is a small toy-app primarily made to experiment various features of the Django Rest Framework.
The app implements a basic ReST client fetching news (in Json format) from random sources located at https://newsapi.org/

The app retrieves the newsapi.org newsfeed every time the user initiates a GET request to the home page.
The news received by the feed are saved to the local database only if they were not already there; (the app compare
the title of the news downloaded with those in the DB to determine what to do).

The list of news rendered for both the HTML and the Json view, however, is retrieved from the database. 

## How to run the project
NewsCrawler project includes a "requirements.txt" file with all the dependencies necessary to run the application.
After you have downloaded the project archive, just run ```pip install -r requirements.txt``` from the project directory,
followed by the usual 
```
manage.py makemigrations
``` 
and 
```
manage.py migrate
```
to generate the data models.

NewsCrawler is distributed without any fixture and/or pre-populated migration files. The database will be filled as soon
as the user open the application homepage. Before getting any response from the newsapi.org API, though, be sure to get 
from their site an API key. 
Copy the key as the value of the ```NEWSAPI_KEY``` variable (in the file ```configuration/settings/DEV_settings```)
to make sure NewsCrawler will work.

## Food for thoughts
* The DB implemented in NewsCrawler is extremely simple, with just a single "Article" class used to store the news
downloaded from newsapi.org. The structure of the Json file retrieved from newsapi.org is actually more complex than that
and NewsCrawler should implement a better domain model.
* The application works synchronously, resulting in several seconds of waiting before displaying the home page. It could
be improved with different approaches like implementing a Redis-like caching technology and a task queue engine like
[Celery](http://docs.celeryproject.org/en/latest/index.html). Just an idea...
* The HTML layout is HORRIBLE! Well, I am a back-end developer who likes ANSI terminals and blinking cursors more than
gorgeous interfaces made with thousands of lines of JavaScript, no wonder.

## Credits
NewsCrawler uses many ideas and code techniques taken from two fundamental books I used to learn almost everything I know
about the django framework: [Django Unleashed](https://django-unleashed.com/) and [Two Scoops of Django](https://www.twoscoopspress.com/). Why try to reinvent the wheel when somebody has already done it for you? :) 

