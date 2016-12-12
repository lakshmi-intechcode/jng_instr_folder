# Phase 2 Assessment - Mini Twitter!

* For your assessment today we'll be building our own mini version of Twitter.
* There should only be `ONE` page load
* Everything after the initial page load should be handled with AJAX calls
* I've posted the user stories below 
* This may sound like a lot or it may sound confusing. Take your time to plan your application. We care more about the quality of your code than how large your code base is. 
* Good luck and feel free to ask questions for clarity.

#### User Stories

* Users should be able to register for an account
* Users should be able to log in 
	* Don't worry about sessions. Assume the user is not closing the window and opening it
* After logging in Users should be able to see all the posts
* Users can make their own post that appear on a personal page
* Users can click a repost button on a post that is not theirs. 
	* It will automatically take that post and put it on their personal page. The page should not reload when the repost button is clicked.

#### Planning

* PLAN OUT YOUR APPLICATION!!!
* Planning lowers the time it takes to develop an app. 
* What will your endpoints be?
* How might your database look like?
	* We'll have at least two models, one for Users and one for posts
	* THINK about this idea of reposting. If a user clicks a repost how will that look in the database? 
* What will your templates look like?
* One template. Use DOM manipulation or Mustache to render the incoming JSON from the server onto the page.

***NOTE!***

* Remember if you create a element dynamically after the page has loaded, you need to attach the proper event listener to that element if it needs an event.


#### Luxury Goals

* Make things look pretty - Honestly your app could look like crap, I just want it to work. If it works then feel free to make it look like better crap.
* Attach CSS styling to it
* Use Mustache.js for templating - Again, Mustache.js isn't needed but if you've tried it recently and you understand it, it can help with showing data dynamically
* Use `hashtags` to tag keywords - Really hard luxury goal
* Add a search bar that can search for those keywords

