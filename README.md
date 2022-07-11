# QuenchMarks

## About This Project

QuenchMarks is a web app that allows you to leave reviews of your favorite water bottles.
You can also favorite your bottles and view reviews by other users.

This project is deployed at: https://quenchmarks.herokuapp.com.

You can log on and test features using this account:

```
username: demomode@test.com
password: testing123
```

## Technologies Used

-   HTML/CSS/JavaScript
    -   Jinja2 Templating Engine
-   Python3
-   Postgresql Database
-   SQLAlchemy ORM
-   Flask Framework to encapsulate all the above

## Todos

-   Build out app [x]
-   Reach MVP (Minimally Viable Product) [x]
-   Style App responsively with Bulma.css [x]
-   Switch database to Postgres from SQLite [x]
-   Deploy to Heroku [x]

## User Stories

-   As a user I can:
    -   look at an index of all bottles [x]
    -   add a new bottle to the website's database [x]
    -   see each individual bottle's info [x]
    -   update bottle's info [x]
    -   delete bottle's info [x]
    -   leave a review for each bottle [x]
    -   select my favorite bottles and display them on my user profile page [x]

## Run this command to have hot reloading on (local cloning only):

```py
FLASK_APP=app.py FLASK_ENV=development flask run
```

## Things Needed for .env

-   DATABASE_URL=
-   SECRET_KEY=
