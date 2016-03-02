# Intro to HTML 

### Learning Objectives
***Students will be able to...***

* Write the boilerplate for an html document
* Utilize HTML and HTML5 tags
* Use inline and block elements with semantic tags

---
### Context

* HTML is not considered a programming language but it is the format of how we visualize information on the web

---
### Lesson

##### Part 1 - HTML Introduction

***What is HTML***

* HTML - Hyper Text Markup Language.
* HTML is a string read by your browser. It displays information in the browser window.
* Every browser renders HTML differently

***Is HTML Programming?***

* Ask: Is HTML a programming language? Why or why not?
* HTML is NOT a programming language
* It is not used to perform any logic
* It's only purpose is to display elements in the browser
* Think of it being similar to PDFs

***Emmet for Sublime***

* This is a package for Sublime (and other text editors) that allows you to make HTML boilerplate code quickly.
* You can follow the directions here to install it with Sublime: [https://github.com/sergeche/emmet-sublime](https://github.com/sergeche/emmet-sublime)
* Before trying to master Emmet get comfortable writing HTML by yourself

***HTML TREE***

* Your HTML document will consist of various elements
* Provide HTML Boilerplate example with Emmets `! tab` command
* `head` - The top of your document
	* Consists mainly of elements that will connect the document to other files
* `body` - The bottom of your document
	* Consists mainly of elements you want to display
* Elements can be nested
	* The outer element will be the parent and the child elements are those that are contained within

***What are some HTML Tags***

* HTML tags tell the browser how to render the content within
* Almost all tags have an opening and a closing tag

```
	* div
	* ul
	* li
	* h1
```
* Some tags have attributes you can populate

```
	* a tag with href
```

***Five Min Exercise***

* Make a html page
* use the following tags to build a webpage
	* head
	* body
	* div
	* h1
	* h2
	* h3
	* p

##### Part Two - HTML5 Intro

* So what is HTML5?
* HTML5 is a set of standards that represents the best implementation of HTML.
* HTML5 allows for easier collaboration between browsers and users
* They do this using Semantic Tags

***What are Semantic Tags?***

* Semantic tags allow us to provide more information in our HTML markup without changing the structure of the page
* Some browsers may display these elements a little different
* Semantic tags are great for the browser, and the user themselves to know what is going on
* Here are some examples of semantic tags

```
	* article
	* section
	* header
	* footer
	* nave
	* aside
```

***Two Different Element Types***

* There are two types of HTML elements
* Inline vs Block elements
* Block element - an element that cannot have anything next to it even if it does not reach the end of the page.
	* e.g. `div`, `h1`
* Inline Element - This element will be called right after/next to the element it is behind in the markup.
	* e.g. `a href`


***Five Min Exercise***

* Open the `index.html` file in the browser
* Replicate it without looking at the code
