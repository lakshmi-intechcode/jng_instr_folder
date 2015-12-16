# Python with Comp Sci Part 3

### Learning Objectives 
***Students Will Be Able To...***

* Merge Sort
* Quick Sort
* Binary Search Tree

---

### Context

* Moar Shit

---

### Lesson

#### Part 1 - Merge Sort

#### Part 2 - Quick Sort

#### Part 3 - Binary Search Tree

* As you may have guessed this is similar to the Binary Search algorithm we studied on Monday
* This only works with a sorted data set
* Imagine a `tree` of nodes. 
* Each node will have two pointers that point to a left node and right node underneath it. 
* The highest node in the BST is known as the `root`
* All nodes on the left of the `root` must be smaller than the root, and all nodes on the right of the root must be greater than the `root`
* Same thing goes for `current` nodes as you travel down the tree
* A balanced tree is where both sides have the same amount of nodes
* As we traverse a balanced tree n will look like this:
	* n
	* n/2
	* n/4
	* n/8
	* and continue until you find the value you want or when you find your number


![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)

***NOTE***

* Although the regular binary search is a "O(log n)" using it to insert or delete a value is still "O(n)"
* With the binary search tree searching, inserting, and deleting, are all "O(log n)"

#### Resources

* [CS50 Merge Sort](https://www.youtube.com/watch?v=EeQ8pwjQxTM)
* [Binary Search Tree Wiki](https://en.wikipedia.org/wiki/Binary_search_tree)
* [Binary Search Tree Youtube Video](https://www.youtube.com/watch?v=pYT9F8_LFTM)