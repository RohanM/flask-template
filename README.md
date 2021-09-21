# Flask + Tailwind + pytest Template


## Getting Started

Install pipenv:

```
pip install pipenv
```

Install dependencies (both Python and JS):

```
pipenv install
npm install
```

Build assets:

```
npm run webpack:dev
# or
npm run webpack:prod
```

Configure the database (to override the SQLite default):

```
echo "export FLASK_TEMPLATE_DATABASE_URI='mydb://user:pass@localhost/db'" >> .env
```

```
pipenv run load-schema
```

Run the development server:

```
pipenv run server
```

Run tests:

```
pipenv run test
# or
pipenv run test-watch
```


## Deployment

The production database URL is configured via the `FLASK_TEMPLATE_DATABASE_URI` environment variable. For
instructions for PythonAnywhere hosting, see:

https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/

To initialise the production database:

```
pipenv run load-schema
```


## Licence

Copyright Rohan Mitchell, released under MIT licence.
