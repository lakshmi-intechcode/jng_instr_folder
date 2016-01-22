# Put things where you want!

### Learning Objectives
***Students will be able to...***

* Utilize CSS display properties
* Utilize CSS position properties
* Diagram Normal Document Flow
* Use z-index

---
### Context

* HTML is cool and all, but to make things more beautiful we'll be using CSS

---
### Lesson

##### Part 1 - Different Display Types

* Before we talk about Normal Document Flow lets do a quick review of the two main display types for elements

***Inline***

* Inline Elements are usually those that define text and data. 
	* `a href`
	* `img` 
	* `span`
	* `strong`
	* `em`
	* `abbr`
* All of these elements will appear in the same line

***Block***

* Block elements will occupy the entire width of their parent container, even if they do not fill out the whole width.
* They are making BLOCKS inside the HTML 
* Almost all of these blocks will have a default padding around them for line breaks.
	* Remember the default style is determined by the browser
* Some block elements are
	* `div`
	* `h1 - h6`
	* `article`
	* `footer`
	* `section`

***BONUS: None and Inline-Block***

* What do you think will happen if we gave an element display none? Pretty much what it says. You're welcome
	* Think about our script tags and head tags.
* Inline-block: You are now allowed to make block elements appear next to each other. Inline-Block display says "Make these elements inline and allow the user to set a width and a height"

##### Part 2 - Normal Document Flow

* Now lets get back to topic of Normal Document Flow
* As we consistently mention, every browser interprets HTML elements differently. 
* Normal Document Flow is how the browser renders your HTML without any CSS or JS. 
* As we know things are read from top to bottom
* What type of displays the elements have also play a hand in the Normal Document Flow
* The screen size also plays a part in how elements appear in the NDF
* [Check out this tutsplus blog for more info on NDF](http://webdesign.tutsplus.com/articles/quick-tip-utilizing-normal-document-flow--webdesign-8199)

##### Part 3 - Box Model Review

* How can we manipulate the position of elements?
* Remember the box model?	
![](http://www.turnwall.com/wp-content/uploads/2014/06/box-model-css.png?670861)

* We can also target all of these and change just one side using `top`, `right`, `bottom`, `left`


##### Part 4 - `%`, `px`, `em`, `rem`, and `auto`
  
* Before we continue lets talk briefly about the different css measurements
* `px`: is a static unit of measure and will stay the same no matter what screen size
* `em`: relative measurement. 1em = 16px. Elements with `em` will scale to the size of it's parent element
* `rem`: stands for `Root em` and is also a relative measurement. `rem` is almost the same as `em` except it is relative to the ROOT font size.
* `%`: always relative to the parent element. When measuring height, the height of the container MUST be set. There is always a default width to a screen size but not a default height
* `auto`: allows us to tell an element to resize itself with regards to it's content. A block level element 	with height auto will grow with more text. With margin auto it will increase it's margins to be centered with the y-axis

***Tips and Resources***

* [StackOverFlow meaning of Auto](http://stackoverflow.com/questions/4471850/what-is-the-meaning-of-auto-value-in-a-css-property)
* [em vs rem](https://j.eremy.net/confused-about-rem-and-em/)

##### Part 5 - Different Positions

* CSS gives us the `position` property to help us format out HTML better.
* They are:
	* `float`
	* `fixed`
	* `absolute`
	* `relative`
	* `static`

***STATIC***

* The default position
* Does not count as being positioned

***FLOATS***

* WE NEVER USE FLOATS
* Floats takes elements out of the NDF
* Take a look at the two examples below and how the text is forced to wrap around the image. 
    -  ```float: right```: ![](http://xhtml.com/510ACA5B-DC0D-4E03-B6BF-861FD62E91F3/float-right.gif)
    - ```float: left```: ![](http://xhtml.com/510ACA5B-DC0D-4E03-B6BF-861FD62E91F3/float-left.gif)

- Every HTML elements that follows a floating element will flow around it. For instance if you have a paragraph that extends longer than an image it will flow underneath it. To avoid this, use the `clear` property. 
- ```clear: left;``` will "turn off" the left floating of elements
* I WILL NOT BE DEMOING THIS BECAUSE WE WILL NEVER BE USING FLOATS

***FIXED***

* Fixed position will always be relative to the browser. 
* It will stay on the screen even if the user scrolls up or down

***ABSOLUTE***

* NEVER USE ABSOLUTE!!!
* It removes elements from the NDF
* If a child element has position absolute the parent will act as if the child is not there
* The element with position absolute will work relative to it's direct parent BUT the parent and all other elements will not recognize a element with position absolute

***RELATIVE***

* 



















##### Part 1 - What is CSS?

* Block vs Inline Elements
* inline block
* pseudo classes
* ul#menu li vs ul#menu > li
* Normal Document Flow
* absolute
* relative
* fixed
* static
* z-index
* floats and clear


##### Absolute Positioning

* Notice where the classes are in the html file, is how they are placed on the page
* If you switch around the colors, they will overlap each other differently
* NEVER use absolute positioning. It takes items out of the Normal Document Flow

##### 







###Part Four - Student Presentations
* Instructor: Watch student demonstation and ensure correctness of findings
* Students: Split into pairs to research a specific position property, come to the board with stickies to predict placement

- Students have 15 minutes to research on their own:
  - relative positioning
  - absolute positioning
  - z-index
  
Instructor presents a scenario. Studnets come up to move the stickies according to the code.

###Part Five - Instructor Summary
*Instructor*: Talking
*Students*: Listening

- **```position:relative```** Position adjusts according to where the element would have been in the Normal Document Flow. Space the element would have occupied stays "reserved" within document flow. Other elements don't collapse around it. Relative positioning behaves the same way as static positioning unless you add properties: ```top```, ```bottom```, ```left```, ```right```

- **```position:absolute```** Removes the element from the Normal Document Flow and positions it relative to its nearest positioned parent element (otherwise, relative to the ```<BODY>``` element). Other elements collapse around it (and appear hidden "behind" the element that has absolute positioning). 

- **`position:fixed`** Use this when you want to keep an element in the same spot in the browser no matter where the user is

- **```z-index```** Assigns an element a "layer number". Higher numbers appear in front of lower numbers. Think Photoshop layers. Requires use of the ```position``` property.


###Part Six - Match the Picture Lab
* Instructor: Walking around, answering questiond
* Students: Coding, Match the picture lab

####Resources
  - [http://learnlayout.com/](http://learnlayout.com/)
  - [http://www.barelyfitz.com/screencast/html-training/css/positioning/](http://www.barelyfitz.com/screencast/html-training/css/positioning/)



#CSS Positioning
####*or*
##How to Put the Elements of Your Blog Wherever You Want


###Learning Objectives

**Use CSS to position elements on a page to reflect a certain desired layout**



- Explain document flow in HTML.
- Use floats to move elements to the left or right border of their containing element.
- Use clear to ensure that an element containing a floating element will stretch to contain its floating child elements.
- Alter an element's default (static) position.
- Use relative positioning to move a child element relative to its parent/containing element.
- Use absolute position to remove an element from document flow and 'force' it's position at a certain point within the flow of the document.
- Use fixed positioning to remove an element from the document flow and 'force' it's position at a certain point within the flow of the document, where it will remain relative to the viewport.
- Use z-index to control the display hierarchy of overlapping elements.

##Part One
Instructor: conversation, Demos Normal Document Flow with sticky notes

Students: laptops closed, watching, answering questions, whatever.

#### What is document flow, how do websites achieve certain layout effects?
- **Normal Document Flow**: How a page is presented when you do nothing to it with regard to structural styling.

- Check out: http://cdn.tutsplus.com/webdesign/uploads/legacy/tuts/367_doc_flow/demo2.html Use the Chrome developer tools to sope out the Normal Document Flow. Discuss the concept of document flow. How can we change it? What does the code look like for this? Look at a blog example. It's a waterfall. 

- HTML elements have a default ```display``` property: ```block```, ```inline```, or ```none```

- **Block-level Elements**: A block-level element always starts on a new line and takes up the full width available (stretches out to the left and right as far as it can):
  - ```<div>```, ```<header>```, ```<footer>```, ```<article>```, ```<section>``` ( tags often used as a container for other HTML elements)
  - ```<h1>``` .. ```<h6>```
  - ```<p>```
  - ```<form>```
  - etc.

- **Inline Elements**: An inline element does not start on a new line and only takes up as much width as necessary.
  - ```<span>```
  - ```<img>```
  - ```<a>```

- Elements such as ```script``` won't display at all 

##Part Two - Review of Positioning Basics
Instructor: Guided practice

Students: Following along using the Developer Tools to examine and modify the Padding, Margins, and Borders of Block-level container elements

- What are the ways we can manipulate the position of elements?  **Padding, Margins, and Borders**
- The Box Model:
![](http://www.turnwall.com/wp-content/uploads/2014/06/box-model-css.png?670861) 
- The horizontal position and size of a block-level element is "normally" determined by setting property values:
  * ```margin-left```, ```margin-right```, ```margin-top```, ```margin-bottom```
  * ```border-left```,  ```border-right```, etc.
  * ```padding-left```, ```padding-right```, etc.
  * ```width``` 
  * ```max-width```, ```min-width```
  * ```border-width```
  * ```padding```
  * etc. 
  
- Set these properties by specifying the size in pixels (```10px```), percentages (```60%```), or ```auto```

Example with padding: http://cdn.tutsplus.com/webdesign/uploads/legacy/tuts/367_doc_flow/demo4.html 



###Part Three - Instructor Demo of ```float``` positioning
* Instructor: float/clear using sticky and code
* Students: Closed Computers

- CSS allows you to set a position property. We can use this property to change positioning! Wee! 
    - ```position:static```
    - ```position:relative```
    - ```position:absolute```
    - ```float```

- Explanation of ```float``` positioning, which pulls an element out of the Normal Document Flow
  - The ```float``` property can be used to wrap text around images
    -  ```float: right```: ![](http://xhtml.com/510ACA5B-DC0D-4E03-B6BF-861FD62E91F3/float-right.gif)
    - ```float: left```: ![](http://xhtml.com/510ACA5B-DC0D-4E03-B6BF-861FD62E91F3/float-left.gif)

- Every HTML elements that follows a floating element will flow around it. To avoid this, use the ```clear``` property. 
- ```clear: left;``` will "turn off" the left floating of elements

Demo example for floating: 


###Part Four - Student Presentations
* Instructor: Watch student demonstation and ensure correctness of findings
* Students: Split into pairs to research a specific position property, come to the board with stickies to predict placement

- Students have 15 minutes to research on their own:
  - relative positioning
  - absolute positioning
  - z-index
  
Instructor presents a scenario. Studnets come up to move the stickies according to the code.

###Part Five - Instructor Summary
*Instructor*: Talking
*Students*: Listening

- **```position:relative```** Position adjusts according to where the element would have been in the Normal Document Flow. Space the element would have occupied stays "reserved" within document flow. Other elements don't collapse around it. Relative positioning behaves the same way as static positioning unless you add properties: ```top```, ```bottom```, ```left```, ```right```

- **```position:absolute```** Removes the element from the Normal Document Flow and positions it relative to its nearest positioned parent element (otherwise, relative to the ```<BODY>``` element). Other elements collapse around it (and appear hidden "behind" the element that has absolute positioning). 

- **```z-index```** Assigns an element a "layer number". Higher numbers appear in front of lower numbers. Think Photoshop layers. Requires use of the ```position``` property.


###Part Six - Match the Picture Lab
* Instructor: Walking around, answering questiond
* Students: Coding, Match the picture lab




####Resources
  - http://learnlayout.com/
  - http://www.barelyfitz.com/screencast/html-training/css/positioning/