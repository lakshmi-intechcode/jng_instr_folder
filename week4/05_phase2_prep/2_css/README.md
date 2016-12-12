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
* We use this for everything from controlling colors, to sizing, to positions, and the like

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

* Check out [www.example.com](http://www.example.com/)
* Open up the inspector. `Do this by right clicking on the page and clicking on inspector`
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

* Sometimes you may see your elements look like below. 

```
	<h1 style="color:red; font-size:70px"> Your website header</h1>
```
* Inline styling was something done during the "old" days of the web when HTML pages were static and didn't have much in terms of content/user interaction
* Some newer libraries utilize Inline CSS. 
* For the purposes of this class we will NOT be using inline styling

***Internal Style Sheet***

* You also have the ability to put CSS styling directly into your HTML file by putting it inside the `<head>` tag
* It will look like this:

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
* Some newer libraries may prefer internal styling but we will STILL NOT DO IT THIS WAY IN THIS COURSE

***External Style Sheet***

* For the purposes of this program we will be putting all our css into their own files. `Seperation of Concerns`
* Keep it in it's own file!
* You can link this file to your HTML using a `link` tag in the head

```
	<head>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
```
* `style.css` is the css file name in the same directory. If it is located elsewhere or named something else you would change this accordingly. e.g. `href=public/stylesheets/style.css`

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
* The hierarchy of what takes precedent over what is as follows:
	* `Inline`
	* `ID`
	* `Class`
	* `TagName`
	
##### Take a look at the example `index.html` and `style.css` to see how this can be incorporated.
