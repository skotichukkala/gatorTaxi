import sys

class Taxi:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration
#Implementation of Min Heap
class MinHeap:
    def __init__(self):
        self.heap_tree = []
        self.positionsno = {}
    #Function for inserting node into Min heap
    def insert(self, rideno):
        self.heap_tree.append(rideno)
        indexno = len(self.heap_tree)-1
        self.positionsno[rideno.rideNumber] = indexno
        self._heapify_up(indexno)
    #Function for getting minimum value
    def extract_min(self):
        if len(self.heap_tree) == 0:
            return None
        if len(self.heap_tree) == 1:
            rideno = self.heap_tree.pop()
            self.positionsno.pop(rideno.rideNumber)
            return rideno
        minimum_val = self.heap_tree[0]
        self.heap_tree[0] = self.heap_tree.pop()
        self.positionsno.pop(minimum_val.rideNumber)
        self.positionsno[self.heap_tree[0].rideNumber] = 0
        self._heapify_down(0)
        return minimum_val
    #Function for deleting a ride from min heap_tree
    def delete(self, rideno):
        if len(self.heap_tree) == 0:
            return False
        if rideno.rideNumber not in self.positionsno:
            return False
        indexno = self.positionsno[rideno.rideNumber]
        self.heap_tree[indexno] = self.heap_tree[-1]
        self.positionsno[self.heap_tree[-1].rideNumber] = indexno
        self.heap_tree.pop()
        del self.positionsno[rideno.rideNumber]
        if indexno == len(self.heap_tree):
            return True
        self._heapify_up(indexno)
        self._heapify_down(indexno)
        return True
    #Function for setting ride into its correct position in upward direction
    def _heapify_up(self, idno):
        prtNodevalue = (idno - 1) // 2 # parent Node
        if prtNodevalue >= 0 and (self.heap_tree[prtNodevalue].rideCost > self.heap_tree[idno].rideCost or (self.heap_tree[prtNodevalue].rideCost == self.heap_tree[idno].rideCost and self.heap_tree[prtNodevalue].tripDuration > self.heap_tree[idno].tripDuration)):
            self.swap_function(idno, prtNodevalue)
            self._heapify_up(prtNodevalue)
    #Function for setting ride into its correct position in downward direction
    def _heapify_down(self, idno):
        leftchild = idno * 2 + 1
        rightchild = idno * 2 + 2
        minvalue = idno
        if (leftchild < len(self.heap_tree) and 
            (self.heap_tree[leftchild].rideCost < self.heap_tree[minvalue].rideCost or 
             (self.heap_tree[leftchild].rideCost == self.heap_tree[minvalue].rideCost and 
              self.heap_tree[leftchild].tripDuration < self.heap_tree[minvalue].tripDuration))):
            minvalue = leftchild
        if (rightchild < len(self.heap_tree) and 
            (self.heap_tree[rightchild].rideCost < self.heap_tree[minvalue].rideCost or 
             (self.heap_tree[rightchild].rideCost == self.heap_tree[minvalue].rideCost and 
              self.heap_tree[rightchild].tripDuration < self.heap_tree[minvalue].tripDuration))):
            minvalue= rightchild
        if minvalue != idno:
            self.swap_function(idno, minvalue)
            self._heapify_down(minvalue)
    #Function for swapping
    def swap_function(self, a, b):
        self.positionsno[self.heap_tree[a].rideNumber] = b
        self.positionsno[self.heap_tree[b].rideNumber] = a
        self.heap_tree[a], self.heap_tree[b] = self.heap_tree[b], self.heap_tree[a]
#implementation of class node
class Node():
    def __init__(self, data_value):
        self.data_value = data_value  # holds the key
        self.parent_node = None #pointer to the parent
        self.left_child = None # pointer to left child
        self.right_child = None #pointer to right child
        self.color_no = 1 # 1 . Red, 0 . Black


# Implementation of Red black trees
class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color_no = 0
        self.TNULL.left_child = None
        self.TNULL.right_child = None
        self.root_value = self.TNULL

    def helper_pre_order__(self, node_key):
        if node_key != self.TNULL:
            sys.stdout.write(node_key.data_value + " ")
            self.helper_pre_order__(node_key.left_child)
            self.helper_pre_order__(node_key.right_child)

    def helper_in_order__(self, node_key):
        if node_key != self.TNULL:
            self.helper_in_order__(node_key.left_child)
            sys.stdout.write(node_key.data_value + " ")
            self.helper_in_order__(node_key.right_child)

    def helper_post_order__(self, node_key):
        if node_key != self.TNULL:
            self.helper_post_order__(node_key.left_child)
            self.helper_post_order__(node_key.right_child)
            sys.stdout.write(node_key.data_value + " ")
    #Function for handling searching tree
    def helper_search_tree__(self, node_key, key_value):
        if node_key == self.TNULL or key_value == node_key.data_value:
            return node_key

        if key_value < node_key.data_value:
            return self.helper_search_tree__(node_key.left_child, key_value)
        return self.helper_search_tree__(node_key.right_child, key_value)

    # Function for fixing tree after deleting node
    def fixing_delete__(self, x):
        while x != self.root_value and x.color_no == 0:
            if x == x.parent_node.left_child:
                s = x.parent_node.right_child
                if s.color_no == 1:
                    s.color_no = 0
                    x.parent_node.color_no = 1
                    self.rotating_left_(x.parent_node)
                    s = x.parent_node.right_child

                if s.left_child.color_no == 0 and s.right_child.color_no == 0:
                    s.color_no = 1
                    x = x.parent_node
                else:
                    if s.right_child.color_no == 0:
                        s.left_child.color_no = 0
                        s.color_no = 1
                        self.rotaing_right__(s)
                        s = x.parent_node.right_child

                    
                    s.color_no = x.parent_node.color_no
                    x.parent_node.color_no = 0
                    s.right_child.color_no = 0
                    self.rotating_left_(x.parent_node)
                    x = self.root_value
            else:
                s = x.parent_node.left_child
                if s.color_no == 1:
                    s.color_no = 0
                    x.parent_node.color_no = 1
                    self.rotaing_right__(x.parent_node)
                    s = x.parent_node.left_child

                if s.left_child.color_no == 0 and s.right_child.color_no == 0:
                    s.color_no = 1
                    x = x.parent_node
                else:
                    if s.left_child.color_no == 0:
                        s.right_child.color_no = 0
                        s.color_no = 1
                        self.rotating_left_(s)
                        s = x.parent_node.left_child 

                  
                    s.color_no = x.parent_node.color_no
                    x.parent_node.color_no = 0
                    s.left_child.color_no = 0
                    self.rotaing_right__(x.parent_node)
                    x = self.root_value
        x.color_no = 0
    #Function for transplanting values in red black tree
    def red_black_transplant(self, u, v):
        if u.parent_node == None:
            self.root_value = v
        elif u == u.parent_node.left_child:
            u.parent_node.left_child = v
        else:
            u.parent_node.right_child = v
        v.parent_node = u.parent_node
    #Function for handling deletion
    def helper_delete_node__(self, node_key, key_value):
        z = self.TNULL
        while node_key != self.TNULL:
            if node_key.data_value == key_value:
                z = node_key

            if node_key.data_value <= key_value:
                node_key = node_key.right_child
            else:
                node_key = node_key.left_child

        if z == self.TNULL:
            return

        y = z
        y_original_color = y.color_no
        if z.left_child == self.TNULL:
            x = z.right_child
            self.red_black_transplant(z, z.right_child)
        elif (z.right_child == self.TNULL):
            x = z.left_child
            self.red_black_transplant(z, z.left_child)
        else:
            y = self.minimum_key(z.right_child)
            y_original_color = y.color_no
            x = y.right_child
            if y.parent_node == z:
                x.parent_node = y
            else:
                self.red_black_transplant(y, y.right_child)
                y.right_child = z.right_child
                y.right_child.parent_node = y

            self.red_black_transplant(z, y)
            y.left_child = z.left_child
            y.left_child.parent_node = y
            y.color_no = z.color_no
        if y_original_color == 0:
            self.fixing_delete__(x)
    
    # Function for fixing red black tree after performing insert operation
    def  fixing_insert(self, k):
        while k.parent_node.color_no == 1:
            if k.parent_node == k.parent_node.parent_node.right_child:
                u = k.parent_node.parent_node.left_child 
                if u.color_no == 1:
                    u.color_no = 0
                    k.parent_node.color_no = 0
                    k.parent_node.parent_node.color_no = 1
                    k = k.parent_node.parent_node
                else:
                    if k == k.parent_node.left_child:
                        k = k.parent_node
                        self.rotaing_right__(k)
                    k.parent_node.color_no = 0
                    k.parent_node.parent_node.color_no = 1
                    self.rotating_left_(k.parent_node.parent_node)
            else:
                u = k.parent_node.parent_node.right_child 

                if u.color_no == 1:
                    u.color_no = 0
                    k.parent_node.color_no = 0
                    k.parent_node.parent_node.color_no = 1
                    k = k.parent_node.parent_node 
                else:
                    if k == k.parent_node.right_child:
                        k = k.parent_node
                        self.rotating_left_(k)
                    k.parent_node.color_no = 0
                    k.parent_node.parent_node.color_no = 1
                    self.rotaing_right__(k.parent_node.parent_node)
            if k == self.root_value:
                break
        self.root_value.color_no = 0
    #Function for handling print operation
    def helper_print__(self, node_key, indent, last):
        
        if node_key != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node_key.color_no == 1 else "BLACK"
            print(str(node_key.data_value) + "(" + s_color + ")")
            self.helper_print__(node_key.left_child, indent, False)
            self.helper_print__(node_key.right_child, indent, True)
    
    # Function for Pre-Order traversal
    def preorder_traversal(self):
        self.helper_pre_order__(self.root_value)

    # Function for In-Order traversal
    def inorder_traversal(self):
        self.helper_in_order__(self.root_value)

    # Function for Post-Order traversal
    def postorder_traversal(self):
        self.helper_post_order__(self.root_value)

    # Function for searching the tree for the key_value k
    def searchTree_traversal(self, k):
        return self.helper_search_tree__(self.root_value, k)

    # Function for finding the node using minimum key
    def minimum_key(self, node_key):
        while node_key.left_child != self.TNULL:
            node_key = node_key.left_child
        return node_key

    # Function for finding the node using maximum key
    def maximum_key(self, node_key):
        while node_key.right_child != self.TNULL:
            node_key = node_key.right_child
        return node_key

    # Function for finding the successor of node
    def successor_node(self, x):
        if x.right_child != self.TNULL:
            return self.minimum_key(x.right_child)

       
        y = x.parent_node
        while y != self.TNULL and x == y.right_child:
            x = y
            y = y.parent_node
        return y

    # Function for finding the predecessor of  node
    def predecessor_node(self,  x):
        if (x.left_child != self.TNULL):
            return self.maximum_key(x.left_child)

        y = x.parent_node
        while y != self.TNULL and x == y.left_child:
            x = y
            y = y.parent_node

        return y

    # Function for rotating left_child at given node x
    def rotating_left_(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child != self.TNULL:
            y.left_child.parent_node = x

        y.parent_node = x.parent_node
        if x.parent_node == None:
            self.root_value = y
        elif x == x.parent_node.left_child:
            x.parent_node.left_child = y
        else:
            x.parent_node.right_child = y
        y.left_child = x
        x.parent_node = y

    # Function for rotating right_child at node x
    def rotaing_right__(self, x):
        y = x.left_child
        x.left_child = y.right_child
        if y.right_child != self.TNULL:
            y.right_child.parent_node = x

        y.parent_node = x.parent_node
        if x.parent_node == None:
            self.root_value = y
        elif x == x.parent_node.right_child:
            x.parent_node.right_child = y
        else:
            x.parent_node.left_child = y
        y.right_child = x
        x.parent_node = y

    # Function for inserting key in appropriate position and fixing tree
    def inserting_key(self, key_value):
    
        node_key = Node(key_value)
        node_key.parent_node = None
        node_key.data_value = key_value
        node_key.left_child = self.TNULL
        node_key.right_child = self.TNULL
        node_key.color_no = 1 

        y = None
        x = self.root_value

        while x != self.TNULL:
            y = x
            if node_key.data_value < x.data_value:
                x = x.left_child
            elif node_key.data_value > x.data_value:
                x = x.right_child
            else:
                pass
        node_key.parent_node = y
        if y == None:
            self.root_value = node_key
        elif node_key.data_value < y.data_value:
            y.left_child = node_key
        else:
            y.right_child = node_key
        if node_key.parent_node == None:
            node_key.color_no = 0
            return
        if node_key.parent_node.parent_node == None:
            return
        self.fixing_insert(node_key)

    def getting_root_value(self):
        return self.root_value

    # function for deleting the node 
    def deleting_node_value(self, data_value):
        self.helper_delete_node__(self.root_value, data_value)

    
    def printing_pretty__(self):
        self.helper_print__(self.root_value, "", True)
#Function for inserting rides        
def inserting_Rides(bst,heap_tree,s,rideNumber,rideCost,tripDuration):
    try:
        x=s[rideNumber]
        #print("Duplicate RideNumber")
        return 0
    except:
        s[rideNumber]=[rideCost,tripDuration]
        bst.inserting_key(rideNumber)
        heap_tree.insert(Taxi(rideNumber,rideCost,tripDuration))
        return 1
#Funtion for printing one ride
def printing_ride_1(bst,heap_tree,s,rideNumber):
    try:
        return [rideNumber,s[rideNumber][0],s[rideNumber][1]]
    except:
        return [0,0,0]
#Function for printing rides between 2
def printing_rides_2(root_value,heap_tree,s,x,rideNumber1,rideNumber2):
    flag = 1
    try:
        printing_rides_2(root_value.left_child,heap_tree,s,x,rideNumber1,rideNumber2)
        if root_value.data_value >= rideNumber1 and root_value.data_value <= rideNumber2:
            x.append([root_value.data_value,s[root_value.data_value][0],s[root_value.data_value][1]])
        else:
            pass
        printing_rides_2(root_value.right_child,heap_tree,s,x,rideNumber1,rideNumber2)
    except:
        pass
    #Function for getting next ride
def getting_next_ride_1(bst, heap_tree, s):
    x = heap_tree.extract_min()
    try:
        p = x.rideNumber
        bst.deleting_node_value(p)
        s.pop(p)
        return [x.rideNumber,x.rideCost,x.tripDuration]
    except:
        return "No active ride requests"
#Function for cancelling ride
def cancelling_ride(bst,heap_tree,s,rideNumber):
    try:
        bst.deleting_node_value(rideNumber)
        heap_tree.delete(Taxi(rideNumber,s[rideNumber][0],s[rideNumber][1]))
        s.pop(rideNumber)
    except:
        pass
#Function for updating rides
def updating_rides_1(bst,heap_tree, s, rideNumber, newTD):
    try:
        x = s[rideNumber][1]
        if newTD < x:
            heap_tree.delete(Taxi(rideNumber,s[rideNumber][0],s[rideNumber][1]))
            heap_tree.insert(Taxi(rideNumber,s[rideNumber][0],newTD))
            s[rideNumber][1]=newTD
        elif newTD > x and newTD < 2* x:
            heap_tree.delete(Taxi(rideNumber,s[rideNumber][0],s[rideNumber][1]))
            heap_tree.insert(Taxi(rideNumber,s[rideNumber][0]+10,newTD))
            s[rideNumber][0]=s[rideNumber][0]+10
            s[rideNumber][1]=newTD
        elif newTD>2*x:
            heap_tree.delete(Taxi(rideNumber,s[rideNumber][0],s[rideNumber][1]))
            bst.deleting_node_value(rideNumber)
            s.pop(rideNumber)
    except:
        pass
if __name__ == "__main__":
    bst = RedBlackTree()
    heap_tree = MinHeap()
    s = dict()
    #takes file name from command line
    with open(sys.argv[1], "r") as f, open("output_file.txt", "w") as fo:
        flag = True
        
        while flag:
            x = f.readline()
            #Performing insert
            if "Insert" in x:
                new_str = x[7:-2]
                numbers = new_str.split(",")
                ride_number, ride_cost, trip_duration = map(int, numbers)
                flag = inserting_Rides(bst, heap_tree, s, ride_number, ride_cost, trip_duration)
                if flag == 0:
                    fo.write("Duplicate RideNumber\n")
            #performing GetNextRide
            elif "GetNextRide" in x:
                l = getting_next_ride_1(bst, heap_tree, s)
                fo.write("("+str(l[0])+","+str(l[1])+","+str(l[2])+")\n" if l != "No active ride requests" else "No active ride requests\n")
            #performing Print ride
            elif "Print" in x:
                new_str = x[6:-2]
                numbers = new_str.split(",")
                if len(numbers) == 1:
                    l = printing_ride_1(bst, heap_tree, s, int(numbers[0]))
                    fo.write("("+str(l[0])+","+str(l[1])+","+str(l[2])+")\n")
                else:
                    p = []
                    printing_rides_2(bst.root_value, heap_tree, s, p, int(numbers[0]), int(numbers[1]))
                    string = ",".join(["("+str(i[0])+","+str(i[1])+","+str(i[2])+")" for i in p])
                    fo.write(string[:] + "\n" if string else "(0,0,0)\n")
            #performing update trip
            elif "UpdateTrip" in x:
                new_str = x[11:-2]
                ride_number, new_trip_duration = map(int, new_str.split(","))
                updating_rides_1(bst, heap_tree, s, ride_number, new_trip_duration)
            #performing cancel operation
            elif "Cancel" in x:
                new_str = x[11:-2]
                numbers = new_str.split(',')
                cancelling_ride(bst, heap_tree, s, int(numbers[0]))

    fo.close()
    f.close()