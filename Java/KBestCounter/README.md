# Programming Homework 4 

Please remember that to submit the assignment you must click Mark as Complete under the Education menu in the toolbar.

Please make sure to look at the written portion of this assignment, which is available on Courseworks. 

## Problem 1 (25 pts): k-best values

Assume you are given a sequence of values. We do not know how many elements there are in this sequence. In fact, there could be infinitely many. Only one value is provided at a time. This is also called a "stream" of values. The goal is to be able to retrieve the k-largest elements seen so far at any time.

Complete the class KBestCounter<T extends Comparable<? super T>> that keeps track of the k-largest elements seen so far in a stream of data using a priority queue. The class should have two methods:

* `public void count(T x)` - process the next element in the set of data. This operation should run in the at worst O(log k) time.
* `public List<T> kbest()` - return a sorted (in increasing order) list of the k-largest elements. This should run in O(k log k) time. If you run this method twice in a row, it should return the same values. You need to make sure that the priority queue is restored to contain the same elements after the method is called.

Use `java.util.PriorityQueue`, which implements a min-heap for you. You should never have more than k elements inserted into the Priority Queue at any given time.

You can use the the class `TestKBestCounter` to test your implementation. However, as always, think about additional test cases you may want to add.

## Problem 2 (75 pts): Dijkstra's Algorithm 

### Before you start:
In this project you will work with a graph representing train connections between North American cities (the graph represents train routes in the popular board game [Ticket to Ride](https://boardgamegeek.com/boardgame/9209/ticket-ride).
The file `ttrvertices.txt` contains a list of cities and their (X,Y) coordinates on the map. These are the vertices in the graph. The file `ttredges.txt` lists direct connections between pairs of cities. These links are *bidirectional*, if you can travel from NewYork to Boston, you can get from Boston to NewYork. These are the (undirected) edges of the graph.

For this assignment, we will use Codio's "Virtual Desktop" functionality. Virtual Desktop allows you to run GUI (graphical user interface) applications on Codio and interact with them in a browser window. You should already see a button labeled "Virtual Desktop" in your Codio menu bar. If not, perform the following steps:
 
* Click on Tools > Install Software
* Search for "X Server" and install the package -- this will take a couple of minutes. It may look like Codio got stuck, but it's installing the package as requested -- be patient. 
* Click on Project > Restart Box... and restart the project box. 

You are now ready to test the GUI. Compile all java sources and run the class Display. Then click on "Virtual Desktop" in your codio menu. This should display the map and a user interface. You can find more information about Virtual Desktop [here](https://codio.com/docs/ide/boxes/installsw/gui/).

In this problem you will implement Dijkstra's algorithm on the map.  We are providing a representation for the graph, as well as code to visualize the map and the output of your algorithm.

Carefully read through the classes `Vertex.java` and `Edge.java`, which represent the vertices and edges of a graph. 
You will only have to modify `Graph.java`, which represents a graph and will contain your code implementing Dijkstra's.  The graph representation is essentially identical to the adjacency lists based implementation discussed one discussed in class. You will need to use the instance variable `vertices`, which contains a mapping from city names to `Vertex` instances after the graph is read from the data files.
Note also that `Graph<V>` is generic. V is the data type used to label each vertex. For the ticket to ride map, this will be a `Graph<String>`. 

### Part 1 (15 pts)
Initially the edge cost (distance) for all edges is set to 1.0. We need to compute the actual distances between the cities. The GUI already contains a button for this purpose, but it does not do anything. In the class `Graph`, implement the method `computeAllEuclideanDistances()` which should compute the euclidean distance between all cities that have a direct link, and set the weights for the corresponding edges in the graph. The euclidean distance between two points (ux, uy) and (vx, vy) is defined as sqrt((ux-vx)^2 + (uy-vy)^2). You might want to use `java.lang.Math` to help with the calculation. After recompiling, clicking the button should now display the correct distances. 

### Part 2 (40 pts)
Implement the method `doDijkstra(String s)` in Graph.java. This method should implement Dijkstra's algorithm starting at the city with name s. Use the distances associated with the edges. The method should update the `distance` and `prev` instance variables of the `Vertex` objects. 
Use a `java.util.PriorityQueue` instances as your heap. 

Important: The shortest path cost associated with vertices already on the priority queue can change throughout the algorithm.
There are two approaches for dealing with this situation. The easiest option (which we will use here) is to allow duplicates on the priority queue. Each cost update will create a new entry in the priority queue. Make sure to add objects of an appropriate type to the priority queue, so that you can distinguish two copies of the same vertex, but with different costs. Don't just make the Vertex class implement Comparable based on the cost annotation. Consider what would happen if you had changed the cost of a vertex that is already in the priority queue. 
Also note that when the algorithm visits a vertex a second time (it becomes the min element on the priority queue a second time), this vertex should be ignored. 

The alternative approach (which we will discuss in class and the written homework), is to modify the priority queue implementation, so that it supports an operation called decreaseKey, i.e. it can dynamically adjust the position of entries the heap if their cost changes. You should not pursue this option for this assignment. 

### Part 3 (20 pts)
Implement the method `public List<Edge<V>> getDijkstraPath(V s, V t)`, which first calls `doDijkstra(s)` and then uses the `distance` and `prev` instance variables of the Vertex objects to find the shortest path between s and t. The result of this method should be a list of Edges on the path.
If implemented correctly, the "Draw Dijkstra's Path" button in the GUI should display the shortest path between New York and LA.
