# Simple Discussion Forum API

## Description
This is a simple Discussion Forum API that uses django auth User model with Token Authentication. 

Any user can view all posts. Only authenticated users can create, like, and view posts. 

Authenticated users can edit and delete posts they created.

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development. The latest version of python.
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application.
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development.


## Getting Started

Using this API code is simple, all you need is to create a virtual environment on your machine.
run `pip install -r requirements.txt` from the root directory to
install the requirements stated in the `requirements.txt` file
Don't forget to add your DEBUG and SECRET_KEY variables in the `.env` file in the root folder.
Example of what the `.env` file should look like
```
DEBUG=<bool>
SECRET_KEY=<django_secret_key>

```
After all is set, run the command `python manage.py runserver` which would start the server on port 8000.
Then go to your API client and visit the port 8000 thus: http://127.0.0.1:8000 

This API consists of 6 endpoints.
Example:
```
   To view all posts (GET): http://127.0.0.1:8000/post/all
   To create a new post (POST): http://127.0.0.1:8000/post/new
   To view details about a post (GET): http://127.0.0.1:8000/post/<id>/details
   To edit a post (PUT, PATCH): http://127.0.0.1:8000/post/<id>/edit
   To like or unlike a post (GET): http://127.0.0.1:8000/post/<id>/like
   To delete a post (GET): http://127.0.0.1:8000/post/<id>/delete
```


## License

The MIT License - Copyright (c) 2021 - Rafihatu Bello
