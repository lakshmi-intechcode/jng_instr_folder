# Using Twitter OAuth!

##### Description

* Let's get a small application going that will use the Twitter OAuth

##### Objectives

***SETTING UP***

* Go to the [Twitter Developer Page](https://dev.twitter.com) and make a developer account.
	* Under the developers tab click on "documentation"
	* Check out the Twitter API if and when you have time
	* For now visit the `OAuth` tab
	* Now click `Overview`
	* At this point you should be on a screen that suggests a route for Obtaining Access Tokens.
	* Click on the "Sign in with Twitter" link: They have great step by step documentation on how to implement this
		* [This is where you should end up](https://dev.twitter.com/web/sign-in/implementing)
* You can make an account when creating an application
* [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new)

***NOTE***

* It is highly suggestted you browse the docs for Twitters OAuth and API
* It may seem confusing at first but trust me when I tell you this documentation is way better than the norm


***Continue***

* Complete the application to get the keys and the access tokens.
* Create a new Django project and configure everything as you normally would
* Your callback url endpoint should be the below

```
http://127.0.0.1:8000/twitter/callback
```
* Python comes with a wrapper for Twitter's APIs called `Twython`
* Download [Twython](https://github.com/ryanmcgrath/twython) (`pip3 install twython`).

***Notes and Goals***

* We will have to store the OAuth tokens to the database.
	* BUT remember they won't have anything to store until the user successfully connects to Twitter
	* You can store the User's OAuth token and token secret as a session variable
		* Make sure to look at the "less technical" explanation resource in the lesson plan for clarification
* Once you get the twitter homepage working, and send a tweet, refactor your code to store users in the database too. 
* Anonymous users will have their stuff stored in cookies
* They will have the option to log in using Twitter's OAuth
* If they log in, their OAutho token will be added to the database
* If they want to sign up for your app specifically after logging in, add their Twitter tokens to the database

***(OPTIONAL)Using Default User Model(OPTIONAL)***

* Create a new custom Users Model and module for this project
* In your registration module add 

```
from django.contrib.auth.models import AbstractUser
```
* You will be making a User Model that inherits from [AbstractUser](https://github.com/django/django/blob/master/django/contrib/auth/models.py#L374).
* It will have all the qualities of the built in User that we've used.
* We're going to be able to add columns for storing OAuth tokens to it. 
* Let's add something to our `settings.py`

```
AUTH_USER_MODEL = 'registration.User'
```
* IMPORTANT: You will need to use setattr to set attributes to the User model manually upon Twitter Authentication. 
* Below is an example of how we do this in the `Django shell`

```
u = User.objects.get(name = "Greg")
setattr(u, 'oauth_token', 'hihihi')
print(u.oauth_token)
'hihihi'
```

***Last Hooray***

* Once you have users set up properly, add a form that allows the User to tweet from their account. 
* Once you have that up and running, have their tweet set off an AJAX request, so that you don't reload the whole page when they tweet. 
* While the tweet is being sent, let the user know that the tweet is being sent
	* Check out this sweet [loading icon](http://www.ajaxload.info/)

