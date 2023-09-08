# GatorTaxi
Problem Statement: In project We need to develop a so1ware for Gator Taxi. Gator Taxi
is a ride sharing service. This so1ware should be useful for keeping track of the pending
ride requests for Gator Taxi. Every ride is idenAfied by three parameters, which are
rideNumber, rideCost and tripDuraAon. Our so1ware should be able to perform few
operaAons. They are
1. Print(rideNumber) which should be able print all the three factors in the following
format (rideNumber, rideCost, tripDuraAon)
2. Print (rideNumber1, rideNumber2) which should be able to print all triplets
between those two rideNumber including them
3. Insert (rideNumber, rideCost, tripDuraAon) should add new ride, but the given
rideNumber should be different from already exisAng ones.
4. GetNextRide (), when we call this funcAon, the trip with lowest rideCost should
come
5. CancelRide (rideNumber) should delete the triplet. If there is no such ride, then it
can simply ignore it.
6. UpdateTrip (rideNumber, new_tripDuraAon) we should use this funcAon when the
rider wishes to change the desAnaAon.
For compleAng this we need to Min Heap and Red Black Tree data structures. Both are
Binary Search Trees. Red black tree is also self-balancing tree. Worst case Ame complexity
for both is O(log j)
Implementa0on: I have used Python programming language and the FuncAons that I have
used in my program for implemenAng all the requirements that are menAoned above are
MinHeap Class:
1. insert (): I have used this for adding new element in to heap without losing min
heap property
Space Complexity: O(1)
Time Complexity: O(log j)
2. extract_min (): Used this method for removing minimum element from the heap
without losing min heap property
Space Complexity: O(1)
Time Complexity: O(log j)
3. delete (): Used for deleAng an element from the min heap by maintain its min heap
property
Space Complexity: O(1)
Time Complexity: O(log j)
4. _heapify_up(): This method is used for moving a node in upward direcAon for
maintain min heap property
Space Complexity: O(1)
Time Complexity: O(log j)
5. _heapify_down(): This method is used for moving a node in downward direcAon
for maintain min heap property
Space Complexity: O(1)
Time Complexity: O(log j)
6. Swap_funcAon(): This method is used for swapping posiAons of two nodes. A1er
swapping it will inform the posiAons in the direcAon
Space Complexity: O(1)
Time Complexity: O(1)
RedBlackTree Class:
1. helper_pre_order__(): This method is used for performing pre-order traversal. It
prints data value of each node recursively starAng from root node.
Space Complexity: O(r)
Time Complexity: O(j)
2. helper_in_order__(): This method is used for performing in-order-traversal
Space Complexity: O(r)
Time Complexity: O(j)
3. helper_post_order__(): This method is used for performing post-order-traversal
Space Complexity: O(1)
Time Complexity: O(j)
4. helper_search_tree__(): This funcAon is used for searching binary search tree. It
takes 2 parameters
Space Complexity: O(r)
Time Complexity: O(j)
5. fixing_delete__(): This funcAon is used for fixing red black tree a1er deleAng node
element
Space Complexity: O(1)
Time Complexity: O(log j)
6. red_black_transplant(): This funcAon takes two nodes as inputs and replaces the
sub tree rooted with at node u with sub tree rooted with V.
Space Complexity: O(1)
Time Complexity: O(1)
7. helper_delete_node__(): This funcAon is used for deleAng element and
maintaining red black tree properAes
Space Complexity: O(1)
Time Complexity: O(log j)
8. fixing_insert(): This funcAon is used for fixing red black tree a1er inserAng new
node
Space Complexity: O(1)
Time Complexity: O(log j)
9. helper_print__(): This funcAon prints tree in formabed form a1er coloring red or
black
Space Complexity: O(1)
Time Complexity: O(log j)
10. minimum_key(): This funcAon is used for finding minimum key
Space Complexity: O(1)
Time Complexity: O(r)
11. maximum_key(): This funcAon is used for finding maximum key
Space Complexity: O(1)
Time Complexity: O(r)
12. successor_node(): This funcAon is used for returning smallest key that greater than
given node
Space Complexity: O(1)
Time Complexity: O(r)
13. predecessor_node(): This funcAon is used for returning predecessor for the given
node
Space Complexity: O(1)
Time Complexity: O(r)
14. rotaAng_le1_(): This funcAon is used for performing le1 rotaAon on binary search
tree.
Space Complexity: O(1)
Time Complexity: O(1)
15. rotaAng_right_(): This funcAon is used for performing le1 rotaAon on binary search
tree.
Space Complexity: O(1)
Time Complexity: O(1)
16. inserAng_key(): This funcAon is used for inserAng element in to red black tree with
maintain red black tree properAes
Space Complexity: O(log j)
Time Complexity: O(log j)
17. gedng_root_value(): This funcAon is used for returning root of the tree
18. deleAng_node_value(): This funcAon is used for deleAng a node with specified
value.
Space Complexity: O(1)
Time Complexity: O(log j)
Main Func0ons:
1. inserAng_Rides(): This funcAon is used for inserAng a new node with triplets into
binary search tree and min heap. It returns 1 if it is successful and 0 if it already
exists
Space Complexity: O(1)
Time Complexity: O(log j)
2. prinAng_ride_1(): This funcAon is used for prinAng triplet for given rideNumber
Space Complexity: O(1)
Time Complexity: O(log j)
3. prinAng_rides_2(): This funcAon is used for prinAng triplets between 2 given
rideNumber.
Space Complexity: O(p)
Time Complexity: O(log (j)+k)
4. gedng_next_ride_1(): This funcAon is used for extracAng and returning details of
ride with minimum trip duraAon from the min heap tree
Space Complexity: O(1)
Time Complexity: O(log j)
5. cancelling_ride(): This funcAon is used for removing ride from binary search tree
and min heap tree
Space Complexity: O(1)
Time Complexity: O(log j)
6. updaAng_rides_1(): This funcAon is used for updaAng trip duraAon of the ride and
change its priority in the min heap tree or it may remove it from binary search tree
and min heap tree based on the new tripDuraAon
Space Complexity: O(1)
Time Complexity: O(log j)
(***r means height of the tree, k is number of triplets, j is number of nodes, p means rides that
fall within the range***)
