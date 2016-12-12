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

* Is HTML a programming language? Why or why not?
* HTML is NOT a programming language
* It is not used to perform any logic
* It's only purpose is to display elements in the browser
* Think of think of this as being similar to PDFs

***Emmet for Sublime***

* This is one of the most popular packages for Sublime Text.
* It allows you to make HTML boilerplate code quickly
* You can follow the directions here to install it with Sublime: [https://github.com/sergeche/emmet-sublime](https://github.com/sergeche/emmet-sublime)
* BEFORE YOU BEGIN USING EMMET MAKE SURE YOU UNDERSTAND HOW TO WRITE HTML CODE BY YOURSELF

***HTML TREE***

* Your HTML document will consist of various `elements`
* If you made an `index.html` file and had Emmet already installed you could run the `! tab` command and it will populate the file with HTML boilerplate. Below is what that looks like

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	
</body>
</html>
```

* `head` - The top of your document
	* Consists mainly of elements that will connect the document to other files
	* This is where you can attach your css files
* `body` - The bottom of your document
	* Consists mainly of elements you want to display
* Elements can be nested
	* The outer element will be the parent and the child elements are those that are contained within

##### Take a look at the `index.html` example to follow along with the rest of this Readme
##### To view what the file looks like in the browser right click anywhere on the file when it is open, then click "Open In Browser"

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

##### Part 2 - HTML5 Intro

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

* Almost all elements default to TWO different `display` types
* Inline Elements vs Block Elements
* Block element - an element that cannot have anything next to it even if it does not reach the end of the page.
	* e.g. `div`, `h1`
* Inline Element - This element will be called right after/next to the element it is behind in the markup.
	* e.g. `a href`

