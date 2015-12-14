# Python with Comp Sci

### Learning Objectives
***Students Will Be Able To...***

* Diagram the Linked List concepts
* Diagram the linear and binary search concepts

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
* How do we add a new node in this linked list? 
	* Placing a node X between two nodes B and C
	* Make the pointer on the X node point to the value in the C node 
	* Make the B next pointer point to the X node

```
* temp = B.net
* B.next = X
* X.next = temp
```
* Traveling through an entire linked list one by one is `Big O of n` or "O(n)"
* If nodes next pointer is `null` we know we are at the end of the list

* Check out the CS50 video on Linked List [here](https://www.youtube.com/watch?v=5nsKtQuT6E8)

#### Part 2 - Binary Search and Linear Search

* [Youtube Video One](https://www.youtube.com/watch?v=wNVCJj642n4)
* [Just Binary Search](https://www.youtube.com/watch?v=JQhciTuD3E8)


