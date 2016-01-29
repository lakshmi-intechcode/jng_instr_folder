User Login with Sessions
=========================

Today we'll be learning a bit about [sessions](https://docs.djangoproject.com/en/1.8/topics/http/sessions/) in this exercise. What are sessions aka cookies? The quick and dirty rundown is that sessions allow us to store data in between requests either client-side or server-side. Since HTTP is a stateless protocol (i.e. it does not save data), without sessions, the users would have to log in every time they went to a new page.

#### Set Up

Set up a new project and make your usual `settings.py` tweaks. We're going to be using and extending the `users` app you wrote yesterday. That is, add the users app to this project.

Add this line to settings.py to tell Django to use cookies for session data:
```py
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
```
#### Two different Routes and Refactor

Unless you went above and beyond yesterday, your Users module just creates users. Make two different POST routes, one for user registration and one for logging in existing users. You can make two different templates and link them, or put both forms on the same template. Totally up to you. Both should redirect to the User Welcome page.

#### Hashing Passwords

Before we get to cookies, lets make sure our user data is nice and secure in our DB. We definitely don't want to store passwords as strings in our DB as this is totally insecure. Take a look at this bit of the [Django docs on password management](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#module-django.contrib.auth.hashers)

When a User is created, it should hash their password using [BCrypt](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django). The linked doc above has everything you need to implement this. **FOLLOW THE DIRECTIONS CAREFULLY**. Once installed, go into the Django shell and print a user's password. You'll see that it's a hash, not the password entered (yay security!).

If you want to log in with the same User, you'll need to compare the plain password string input by the User and the encrypted password in the DB. That method is also described in the Django docs linked above. If the password doesn't match, re-render the page (with errors). If it passes, redirect them to their user login page.

#### Sessions Login

Now we're going to store a session key. Sessions are a held in a dictionary as a property of the Request object. You can see all of the keys by printing to your server logs: 
```
    request.session.keys()
```

You can make a new session variable by typing `request.session['yourkey'] = value`. Once you've succesffuly printed the Sessions dictionary, let's store a new session on log in and create. If the user successfully logs in, lets store a user_id key with the user's id as the value.

Take a look at this exmaple with pseudocode:
```python
def user_login(request):
    username, password = request.POST['username'], request.POST['password']
    # Check if form values are valid
        # if valid:
            # try to query DB for user
                #if the user exists
                    #verify passwords
                        #if username and passwords match:
                            # SET session key her
                            # return redirect to user page
        # else return redirect with errors
````

Now change your user welcome page, so that instead of taking a user id or user name as a captured URL value / view function argument, it loads the User object from the DB based on the user_id stored in the session.

```python
def welcome_page(request):
    #if session with user_is found;
        # query user
        # render user page with retrieved user information
    #else:
        # send them to login page
```

At the beginning of this view, make sure that the user_id session variable exists. If it doesn't that means the user isn't logged in and should be redirected back to the login page. `session.get` will help with this.

#### Logout

Make a logout page that clears the session when the user hits the route, then redirects back to the homepage. Hint: Django has a built in function for this. What is it?

#### Expiration

Let's add an expiration to our session. Look through the session docs and see if you can find something that sets an expiration. After login have their session expire in a few seconds, refresh the page and watch it work.
