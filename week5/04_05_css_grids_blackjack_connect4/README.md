# CSS Grids

### Learning Objectives
***Students will be able to...***

* Use CSS Reset
* Use CSS Normalize
* Use CSS Grid layout
* Use CSS Media Queries
* Use CSS Pseudo:classes

---
### Context

* This skill becomes very useful for building responsive design

---
### Lesson

##### Part 1 - Pseudo Classes

* Review different display types
* Review Selectors and Inheritence
* Now introduce Pseudo Classes
* Pseudo Classes will apply specific CSS styling to an element on window onload or through user interaction This allows our page to look more dynamic. Some pseudo-classes are:
	* :active
	* :first-child
	* :last-child
	* :nth-child
	* :hover
	
***NOTE***

* Pseudo Classes ARE NOT JAVASCRIPT. We are manipulating the style of an HTML element using only CSS. 

***SHOW THEM THE HTML CSS EXAMPLE - STOP AT HOVER***

##### Part 2 - CSS Transition

The transition property allows us to control an animations speed. It can take up to four parameters: 

* property - this is the property that the transition is `listening` for.
* duration - how much time it will take to execute
* timing-function - what kind of animation will it be. `ease`, `linear`, `step-end`
* delay - how long before this transition takes effect

***SHOW THEM THE FLASH AND SUPERMAN***

* The Transitions property also gives us control of fading elements

##### Part 3 - Media Queries

***What do media queries do?***

* Media queries allow us to specify styling of HTML content specific to different devices
* They are used for Responsive Design

***Responsive Design***

* Responsive Design allows us to load the same HTML on any device and it will change it's style dynamically
* `Show them the inspector different device view`
* let's make a html file and put this inside the head

```
<meta name="viewport" content="width=device-width,initial-scale=1">
```
* add the following divs to the file

```
<div class="mobile">I am on a phone</div>
<div class="tablet">I am on a tablet</div>
<div class="computer">I am on a computer</div>
```

***Five Min Exercise***

* Can you figure out how to set the tablet to display? 
	* The IPad tablet size is about 1024px
* Can you figure out how to set the computer to display? 
	* The average computer size is, well bigger than a tablet.

***Solution***

* Lets add this inside a style.css file and link that file to the html

```
@media only screen and (max-width: 667px)

.tablet{
	display:none;
}
.computer{
	display:none;
}
```
* Noticed we set a `max-width` to this media query. 
* This styling will only appear on screens less than 667px
* Let's add some more to the stylesheet. This time a `min-width`

```
@media only screen and (min-width: 667px) and (max-width: 1024px)

.mobile{
	display: none;
}
.computer{
	display: none;
}
```
* And finally the computer display

```
@media only screen and (min-width: 1024px)

.mobile .tablet{
	display: none;
}
```

* Change the browser size and check it out
* `Remember to show them the developer console device preview`

***Device width***

* In the meta tag you saw device width instead of width. Now with so many devices having high density retina displays we want to target the physical width of a device.

***Meta Tag***

* The meta tag tells our device it should display the page in relation to the device size. 

***Last Example***

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

##### Part 4 - CSS Reset vs Normalize

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

##### Part 5 - CSS Grids

* What are the different grid systems out there?
	* Skeleton - extremely lightweight. May have a hard time with mobile responsive
	* Pure - A little heavier than skeleton but still much lighter than Bootstrap
	* Foundation - A good mix of templates they offer, still not as heavy as Boostrap
	* Bootstrap - The heaviest CSS grid framework. 
* Why are we using grids
* Grids never used to exist before because there weren't many different screen sizes
* Instead we used "media queries" This leads to very hard to read code in your stylesheet and your HTML 
* The grid system is used to organize your code while allowing you to easily build a responsive site

##### Part 6 - Foundation CSS

* As you may have already heard my favorite CSS Grid Framework is Foundation CSS
* It is Semantic, Clean, very easy to use, constantly growing, and has great documentation. 
* Let's take a look at their [documentation](http://foundation.zurb.com/sites/docs/v/5.5.3/css.html)
* They even offer customizable [Foundation Templates](http://foundation.zurb.com/templates.html)
