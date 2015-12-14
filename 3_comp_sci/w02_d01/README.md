# Python with Comp Sci

### Learning Objectives
***Students Will Be Able To...***

* Diagram the Linked List concepts
* Diagram the linear and binary search concepts
* Answer which search algoritm is faster using Big O Notation

---
### Context

* We are covering some computer science topics to help us think efficiently while programming

---

### Lesson

#### Part 1 - Linked List

* The concept of Linked List is to have a list of values to search through. 
* This sounds similar to an array but it is very different, with it's own advantages and disadvantages
* Linked Lists stores data in `nodes`
* Each node will contain two things. A `value` that node is storing, and a `pointer` that will point to the next node in the list
* The first node in a linked list is known as the `head`
* So how is this different from python list, or arrays in other languages. 
* With linked list we are not storing/declaring our data set initially. Instead we are only looking at one node at a time. This will save us memory. 
* The advantage to this versus an array/list is we do not have to use so much memory to navigate through a list of values. Imagine if we had an extremely large data set. We wouldn't want to store it in memory just to loop through it. 
* The disadvantage to this is since we are not declaring all the values up front we do not have the ability to start a search at a specific point in time. We have to loop through every node until we find what we want. 
* We don't have to declare how big the linked list will be, unlike looping through an array

***Five Min Exercise***

* How do we add a new node in this linked list? 

***Answer***

* Placing a node X between two nodes B and C
* Make the pointer on the X node point to the value in the C node 
* Make the B next pointer point to the X node

```
* temp = B.next
* B.next = X
* X.next = temp

OR more simply

* X.next = C
* B.next = X
```
* The top way with `temp` takes into account how we have to loop through a linked list. The second set in the box is just for demonstration
* Remember that the only sense of direction we get in a linked list is through their `next` pointer. This is the reason why we can't just make 
* Traveling through an entire linked list one by one is `Big O of n` or "O(n)"
* If nodes next pointer is `null` we know we are at the end of the list


#### Part 2 - Big O Notation

* Big O Notation is a way to check/describe how efficient an algorithm is. That is how long it takes to run
* Looping through a list of items in a linear fashion will be a `O(n)`
* Having a loop nested inside of another loop will be an `O(n^2)`
* Using the Binary Search would be a `O(logn)`

***Five Min Exercise***

* What would be the Big O of the following three functions?

```
def the_names():
	for name in people:
		print name
	
	

def your_func():
	for num in numbers:
		print num
	
	for char in characters:
		print char
		
		
		
def my_func():
	for x in xyz:
		for a in abc:
			print x
			
	for i in j:
		print i

```
* We only use the most significant terms
	* If we had a function with two for loops in it it would be `O(2n)`. However, we would drop the 2 from that equation because as n gets expomemtially large the two doesn't matter. 
	* If we had a function with three loops, loop A was a stand alone, and loop C was nested in loop B it would be `O(n + n^2)`. We would drop the smaller n in this equation for the same reason as the previous example

#### Part 3 - Binary Search and Linear Search

* Linear Search is easier to program
	* You are looping through an array one by one until you find what you are looking for
	* "O(n)" - going through each value
* Binary Search is harder to program but more efficient
	* This only works with a sorted array/list	
	* Identify where the middle is, cut this in half, search through that half
	* "O(log n)" - binary search way. this is usually the fastest 


#### Videos and Tutorials

***Big O Notation***

* [Wiki](https://en.wikipedia.org/wiki/Binary_search_algorithm)
* [Interview Cake](https://www.interviewcake.com/article/python/big-o-notation-time-and-space-complexity)

***Linked Lists***

* [CS50 Youtube Video](https://www.youtube.com/watch?v=5nsKtQuT6E8)

***Linear and Binary Search***

* [Youtube Video on both](https://www.youtube.com/watch?v=wNVCJj642n4)
* [Just Binary Search](https://www.youtube.com/watch?v=JQhciTuD3E8)
* [Just Linear Search](https://www.youtube.com/watch?v=iwo5WAldDks)

***Assert Method***

* [Tutorials Point](http://www.tutorialspoint.com/python/assertions_in_python.htm)



