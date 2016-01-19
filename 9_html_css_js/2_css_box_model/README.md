# CSS Intro

### Learning Objectives
***Students will be able to...***

* Format HTML markup using CSS Box Model
* Link CSS stylesheets
* Target elements using CSS specificity
* Style HTML markup using CSS properties
* Use the inspector in Chrome to view CSS styling and HTML markup

---
### Context

* HTML is cool and all, but to make things more beautiful we'll be using CSS

---
### Lesson

##### Part 1 - What is CSS?

* CSS stands for Cascading Style Sheets
* It allows us to control how HTML markup is presented in the browser
* We use this for everything from controlling colors, to size, to positions, and the like

##### Part 2 - Box Model

* As mentioned previously browsers may render HTML differently
* All elements will have default positioning properties. (differ depending on browser)
* This is what we know as the `Box Model`
* There are four layers to the box model
	* Content - wraps the actual content 
	* Padding - layer after content
	* Border - layer after padding
	* Margin - outermost layer

##### Part 3 - Chrome Inspector

* Check out [example.com](www.example.com)
* Open up the Chrome Inspector
* Hover over all the layers of the various elements and check out the box model

***Five Min Exercise***

* Target the h1 element, and on the right hand side add/change the following properties
	* padding-bottom = 50px
	* text-decoration = underline
	* color = red
	* text-align = center
* Target the paragraph element, and add the following properties
	* text-indent = 50px 
	* font-size = 1.2em

##### Part 4 - Hooking Up CSS

* There are three seperate ways to connect CSS to your html file. 

***Inline***

* Sometimes you maye see your elements look like below
	
```
	<h1 style="color:red; font-size:70px"> Your website header</h1>
```
* Inline styling was something done during the old days of the web when HTML pages were static and didn't have much in terms of content/user interaction
* DO NOT use Inline styling. I will throw you out of my class!
	
***Internal Style Sheet***

* You are also able to apply CSS styling directly in your html file
* It will look like this

```
	<head>
		<style>
			h1 {
				color: red;
				font-size: 70px;
			}
		</style>
	</head>
```
* This is much better than Inline but I STILL DO NOT use this. 
* Remember we are programmers and we apply separation of code for organizational purposes

***External Style Sheet***

* The one true way to apply your CSS
* Keep it in it's own file!
* You can link this file to your HTML using a `link` tag in the head

```
	<head>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
```
* `style.css` is the css file name in the same directory. If it is located elsewhere or named something else you would change this accordingly

##### Part 5 - Specificity - How To Target Elements

* Great so we know how to hook up CSS files, but now we have to actually apply CSS properties. 
* CSS stands for Cascading Style Sheets - Keyword here is `Cascading`
* CSS Styles and Properties are defined in a specific sequence. 
* It depends on two things
	* How we connected our CSS: `Inline` vs `Internal` vs `External`
	* What selector we used: `ID` vs `Class` vs `Element`
* What are CSS Selectors?
* Selectors allow us to target a single or a group of html elements
* There are three types of Selectors
	* ID - uses the pound sign, or as some of you may know it as, a hashtag `#`
	* Class - uses the period `.` 
	* Element - uses the elements tag name itself
* Specificity Rules
	* If two elements are targeted by two different selectors the properties that have a higher hierarchy/specificity wins
	* If two elements are targeted by selectors that have the same hierarchy the one that comes later wins.
		* Remember `Cascading!!!`
		

##### HOMEWORK

* Homework tonight for CSS is a little different. 
* There are no prompts. Your goal is to complete the exercises at the below website
* [CSS Diner](http://flukeout.github.io/)




























