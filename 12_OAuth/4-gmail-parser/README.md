Read my Email Please
====================
Using the code you wrote in the previous exercise to authorize users with Google, retrieve an authorized user's email.

###The Gmail API

Enable Gmail for your project in your developer account. Make sure you add the appropriate scope so that you're allowed to retrieve users Gmail.

Here's a [list of API endpoints](http://developers.google.com/apis-explorer/#p/gmail/v1/) for Gmail. You can play with this in your own browser with your own account so figure out what your program needs to request.

###Making Requests

Use the requests library to make GET requests to the proper endpoints.

Figure out the appropriate endpoint, and make requests on behalf of your authorized user. You need to add the "authorization" access token header returned from py-oauth2. Your request should look something like this:
```py
requests.get('gmail/messages', headers = access_token.headers)
```
Tip: the email body is base_64 encoded. You'll need to decode it.

###Sentiment Analysis

Using the sentiment analysis function you wrote yesterday, analyze the sentiment for all emails sent by a specific email address. Allow the user to enter the email address whose correspondence they want to analyze in a form on your site.
