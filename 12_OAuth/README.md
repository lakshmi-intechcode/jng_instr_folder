# OAuth Intro

### Learning Objectives
***Students will be able to...***

* Use OAuth for user authentication

---

### Context

* Allowing trusted third parties to authenticate users for us

---

### Lesson

##### Part 1 - What is OAuth?

* OAuth stands for Open standard for Authentication. 
* It allows us to have a third party validate a users authentication for us. 
* Think about applications/websites that ask you to sign in with your Google Email, or Facebook, or Twitter account instead of having their own
* These applications are essentially saying "I trust Googles / Facebook / Twitter services to verify the user is who they say they are"
* [(MUST READ) Here's a great explanation for OAuth](http://hueniverse.com/oauth/guide/terminology/)
* [OAuth Wiki (technical and boring)](https://en.wikipedia.org/wiki/OAuth)
* [Here's a list of OAuth Providers](https://en.wikipedia.org/wiki/List_of_OAuth_providers)

***A Visual for OAuth***

![OAuth](https://developers.google.com/accounts/images/webflow.png)

* The user will hit your application and be prompted to login through their google account
* If they are verified your App will get back a token. This will be in place of the users Username and Password. 
* You can now use this token to allow the user to call the Google API

##### Part 2 - Extra Extra functionality

* A positive of OAuth is, if you are a smaller application you may trust these other larger companies to verify users. Their security will most likely be better than your own
* Allowing `tokens` from third party sources can also allow us the functionality of those resources. 
* For example we may be allowed to:
	* Link our users to their tweets on twitter
	* Link our users to google maps api

##### Part 3 - Combining OAuth 

* When you allow a user to log in through OAuth you will get back an `access token`
* We want to store their `user_id / unique id` along with their `access token`
* If they exist they are logged in
* If they do not exist you will have to create that user in your own database
* [Check out this stack overflow answer on OAuth login](http://stackoverflow.com/questions/11165088/what-is-the-standard-with-oauth-for-remembering-users)

##### Part 4 - API Keys vs. Auth

* You may be wondering this sounds similar to having an API key, what the hell is the difference?
* [Check out this VERY SHORT blog post for your answer](http://www.srimax.com/index.php/do-you-need-api-keys-api-identity-vs-authorization/)