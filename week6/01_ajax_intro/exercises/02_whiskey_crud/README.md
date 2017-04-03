# Single Page Whiskey App

#### Description

* Visit this github repo:
* [https://github.com/Jingo88/booze_api](https://github.com/Jingo88/booze_api)
* This is a Whiskey API I built in SQLite3, and Express.js
* Inside of the repo there is a README file that will explain how to set it up and use it.

#### Objectives

* Inside of the "views" folder start a `index.html`, `style.css`, and `main.js`
* You will build an single page application that will allow the user to CRUD to the `whiskey.db` from the booze api repo
* Start the whiskey api in a terminal window
* It will run on port 8080
* The endpoints of your ajax calls are inside of the repos README file. You should direct them to `http://localhost:8080/`
* Build your application in the views folder

#### User Stories

* A user should be able to search for a whiskey
* If the whiskey is not there a user should be able to add a whiskey
* If the whiskey is there a user should be able to update that whiskey or delete it
* How can you build the search functionality to include "ALL" whiskeys that have the searched word?

***Notes***

* Use Postman to test the routes of the api to make sure it is working
* Your ajax calls may look something like this

```
GET REQUEST

$.ajax({
    url: "http://localhost:8080/",    
    type: "GET",
    success:function(data){
        console.log("SUCCESS ON GET REQUEST!!!");   
        console.log(data) 
    }
});


POST REQUEST

$.ajax({
    url: "http://localhost:8080/whiskeys",    
    type: "POST",
    data: {
        "name":"BLAH",
        "type":"WINE",
        "price": 35
    },
    success:function(data){
        console.log("SUCCESS POSTING!!!");   
        console.log(data) 
    }
});

```


