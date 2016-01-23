# CSS Grids

### Learning Objectives
***Students will be able to...***

* Use CSS Reset
* Use CSS Normalize
* Use CSS Grid layout

---
### Context

* This skill becomes very useful for building responsive design

---
### Lesson

##### Part 1 - Media Queries

* Take a look at the [w3schools media query example](http://www.w3schools.com/cssref/css3_pr_mediaquery.asp)

***Five Min Exercise***

* Take the image from the below link and put it in an html page

```
https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwizi9Cx38DKAhWI8j4KHRLaDVUQjRwIBw&url=http%3A%2F%2Fmarvel.wikia.com%2Fwiki%2FWolverine_(James_%2522Logan%2522_Howlett)&psig=AFQjCNEak6qWDWtb-FVUjzS6TjibGp9LAg&ust=1453666371701461
```
* Now use media queries to make the following parameters for the image
	* 50% width and on the left side of the screen for full size
	* 50% width and centered when the screen is half sized
	* 100% width when the screen is cell phone sized

##### Part 2 - CSS Reset vs Normalize

* Browsers will render HTML elements differently

***Reset CSS***

* CSS Resets allow us to set a consistent baseline for how various browsers render HTML

***Normalize CSS***

* Normalize CSS keeps useful defaults. 
* This is different from Reset because Reset takes off everything. 
* Normalize is preferred 
* [Normalize CSS CDN](https://cdnjs.com/libraries/normalize)

***Frameworks***

* Many frameworks already incorporate this kind of information so we don't always need to download and use Normalize CSS files

##### Part 3 - CSS Grids

* What are the different grid systems out there?
	* Skeleton - extremely lightweight. May have a hard time with mobile responsive
	* Pure - A little heavier than skeleton but still much lighter than Bootstrap
	* Foundation - A good mix of templates they offer, still not as heavy as Boostrap
	* Bootstrap - The heaviest CSS grid framework. 
* Why are we using grids
* Grids never used to exist before because there weren't many different screen sizes
* Instead we used "media queries" This leads to very hard to read code in your stylesheet and your HTML 
* The grid system is used to organize your code while allowing you to easily build a responsive site

##### Part 4 - Foundation CSS

* As you may have already heard my favorite CSS Grid Framework is Foundation CSS
* It is Semantic, Clean, very easy to use, constantly growing, and has great documentation. 
* Let's take a look at their [documentation](http://foundation.zurb.com/sites/docs/v/5.5.3/css.html)
* They even offer customizable [Foundation Templates](http://foundation.zurb.com/templates.html)
