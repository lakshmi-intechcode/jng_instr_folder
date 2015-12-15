# Python with Comp Sci Part 2

### Learning Objectives 
***Students Will Be Able To...***

* Reverse a string without using the `reverse` method
* Pseudo Code the two sorting algorithms

---
### Context

* A continuation of computer science topics
* These are other sorting algorithms that will teach us how to think efficiently while programming

---
### Lesson

#### Part 1 - Stacks

* Stacks are abstract data types. Like Linked List this is a concept that is programmable in multiple languages
* This follows the LIFO process. (Last In First Out)
* Every `node` holds a `value` and a `pointer` to the next node
* Imagine a list/array turned 90 degrees to be vertical, where the first element is on the bottom and the last element is on the top
* The main methods to quickly display stacks are `pop` and `append` (push in other lanuages)
* `pop` will remove the top node on the stack and return it to you
* `append` will add a node to the top of the stack

**Five Min Exercise**

Without using the `reverse` method reverse the string "Hello World"

#### Part 2 - Queues

* Queues are the opposite of Stacks. They are abstract data types that follows the FIFO process (First In, First Out)
* Imagine an array/list normally (not turned 90 degrees like the stack diagram)
* `Enqueue` - add a node to the end of the queue
* `Dequeue` - to remove a node from the front of the queue

![https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/405px-Data_Queue.svg.png)



#### Part 3 - Bubble Sort

* Bubble sort is one of the simplest algorithms to program but also one of the slowest sorting methods with a "O(n^2)"
* It will iterate through an array/list multiple times and checks if the current value is greater than or less than the next value. If it is then switch the position, if it is not then the next value will now be the current value. Rinse and Repeat

![https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)


#### Part 4 - Insertion Sort

* Insertion sort is another sorting method with a "O(n^2)" but at the same time is more efficient than bubble sort. 
* With insertion we are iterating through the array/list and checking that current value against all the values that we have already passed (the sorted section)

***Five Min Exercise***

* Why is this still considered "O(n^2)"
* Pseudo code this insertion sort and explain


![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

#### Resources

* [Stack Wiki](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
* [Queue Wiki](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
* [Bubble Wiki](https://en.wikipedia.org/wiki/Bubble_sort)
* [Insertion Wiki](https://en.wikipedia.org/wiki/Insertion_sort)









