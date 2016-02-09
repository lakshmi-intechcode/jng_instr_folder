Google Oh Yeah!
===============

Today we're going one step further with OAuth and will authorize Google users into our site.

Google uses a OAuth2, which is slightly different than what we did with Twitter.

###Setup

Register a developer's account at [Google](https://developers.google.com/)

Just add the Google+ app for now, that's all we'll need for this first exercise.

Create a new Django project, and SECURELY store your client_id and client_secret. Set your Google redirect_uri to a route in your Django Project. Something like `http://localhost:8000/oauthcallback`

We're going to be using this generic python3 [oauth2 library](https://github.com/liluo/py-oauth2). Install it and check the README. There's example code for Google - it's very simple and depends on manual input of data. You'll need to customize this snippet to automate the process and make it work seamlessly on the web.

Make sure you have the scopes right - you can read about them [here](https://developers.google.com/+/api/oauth)

###Go!

Using the demo code provided by py-oauth2 and Django, retrieve the user's info, including email address, and store the user and their token in your database for future use.
