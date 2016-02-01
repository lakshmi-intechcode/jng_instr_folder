# Making a To Do API!

##### Description

* Now we're going to make an API for a Todo list using Django
* Like many web APIs, we will not be rendering HTML. 
* We will be creating a web based interface that allows users to interact and perform CRUD operations with our DB
* This interaction will be done using HTTP requests (GET or POST) and our clients will be expecting to send or receive JSON.
* In an API routes/urls are known as `endpoints`
* These `endpoints` are the entry points to the database resources
* We will be following `RESTful` practices when building this API

##### Resources

- [What exactly is RESTful programming?](http://stackoverflow.com/questions/671118/what-exactly-is-restful-programming)
- [Representational State Transfer Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
- [CSRF Exemption for APIs](http://stackoverflow.com/questions/10741339/do-csrf-attack-worries-apply-to-apis)
- [curl](http://superuser.com/questions/149329/what-is-the-curl-command-line-syntax-to-do-a-post-request)




#### Syntax to Know

We're going to use Django's built-in [JsonResponse](https://docs.djangoproject.com/en/1.8/ref/request-response/#jsonresponse-objects) object to send JSON objects to the user. Every endpoint in your API will return JSON, like so:
```py
from django.http import JsonResponse

def get_todos(request, user_key):
    return JsonResponse({"key":"value"})
```
We're going to need to make our endpoints CSRF exempt, for now. We don't need Django's CSRF protection since we want users to be able to perform CRUD operations to our resources. 
```py
from django.views.decorators.csrf import csrf_exempt
# If you're using classbased views, in urls.py
url(r'^stocks$', csrf_exempt(MyView.as_view()))
# If you're using regular views, in views.py
@csrf_exempt
def my_view(request):
    ...
```
Finally, our JSON encoded post data will not be in Django's `request.POST` dictionary. You can find it in `request.body`.

#### The User Model

Our todo list will have `User` and `Todo` models. Include the appropriate fields for each mode. 
    
    class User:
        # name
        # token
        
    class Todo:
        # content
        # user_id
        # created_date
        # updated_date
        # finished


A User will have many Todos. Each user model should be assigned a random key on creation that must be passed with every request(i.e. for authentication purposes)  We're going to use a [*Universally unique identifier*](https://en.wikipedia.org/wiki/Universally_unique_identifier) and pythons [UUID module](https://docs.python.org/3/library/uuid.html#uuid.UUID) to create unique identifiers. Here's how to make that key:
    ```py
    from uuid import uuid4
    key = uuid4().hex
    ```
When a user makes a request, the complete URL should look __something like__ this:

    GET http://mytodolist.com/todos/<user_token>/



#### The Application

As usual, GET and POST routes should be used appropriately. This more for the sake of convention in this case, and not for browser behavior. Make sure to keep your URLs RESTful and ask plenty of questions if anything in unclear.

## Endpoints
#### GET routes

- Create an endpoint that returns all of that User's todos, whether they are finished or not.
- Create an endpoint that only returns that User's incomplete todos.
- Create an endpoint that only returns that User's todos for a given date.

You should be able to use and test these in your browser. All errors due to user submission (bad key, incorrect endpoint) should return a 404 status code to the client.

#### POST routes

To make a proper POST request, you are going to `curl` from your terminal and send in the data to the server.  You will need to pass in the user token as below:
     
     curl -X POST "http://127.0.0.1:8000/todos/" -d "token=81a8d4a4cf0b9c65&todo=buy beer"


* Create an endpoint that saves a new todo to the database for the given user's token.
* Create an endpoint that marks a given todo complete for the given user.
* Create an endpoint that updates a given todo for the given user.
* Create an endpoint that deletes a given todo for the given user.
