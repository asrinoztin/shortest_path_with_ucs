# Introduction

In this project, a road map of certain Turkish cities will be used to apply the Uniform Cost Search (UCS) method to find the shortest route between two cities. Python will be used for the implementation, and the application will be needed to adhere to certain standards. We will outline the UCS algorithm, describe how priority queues are utilized in this project, look at the source code, and then show the test results in this report.

<img width="1039" alt="Ekran Resmi 2023-05-21 18 39 57" src="https://github.com/asrinoztin/shortest_path_with_ucs/assets/58219688/a5edfa87-d726-4d87-90b0-691e4a215796">

# Uniform Cost Search Algorithm

To determine the path that has the lowest cost between two nodes in a network, computer scientists use a variation of the Breadth-First Search (BFS) technique known as Uniform Cost Search. UCS, in contrast to BFS, gives each edge a cost value and prioritizes paths with lower cumulative costs during the search. BFS treats all edges equally. UCS is therefore ideal and always discovers the shortest path if one exists.

Priority queues are used by UCS to organize the untried pathways. The path with the lowest cost is always at the head of the priority queue because it is sorted by path cost. This indicates that UCS investigates the paths in ascending cost order, always choosing the one with the lowest cost at each stage. This allows UCS to efficiently traverse the graph and identify the best path.

UCS is a significant method utilized in numerous computer science applications, including route planning, machine learning, and artificial intelligence. It is an effective tool for addressing complex problems and optimizing solutions since it can locate the shortest path in a graph.

# Usage of Priority Queues in the Project
Priority queues are employed in this project to carry out the UCS algorithm. A tuple (0, start, []) is used to initialize the priority queue. The first value in the tuple indicates the total cost of the path, the second value is the current node, and the third value is a list of all the nodes that have been visited. The first value of the tuple, which is the path's total cost, determines the priority queue's order. The algorithm dequeues the path with the lowest cost from the priority queue after each iteration, investigates its neighbors, and then adds them, with their respective costs, to the priority queue.
