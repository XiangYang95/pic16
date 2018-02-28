import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data);

class LinkedList:
    def __init__(self, data):
        self.first = Node(data)
        self.curr = self.first
        self.last = Node(data)
        self.n = 1
        self.list = []
        self.list.append(self.curr)
        
    def append(self, data):
        k = Node(data)
        if self.first.data == self.last.data:
            self.first.next = k
        self.last.next = k
        self.last = self.last.next
        self.n += 1
        self.list.append(k)
    
    
    def __iter__(self):
        for i in range(self.n):
            if self.curr == None:
                self.curr = self.first
            j = self.curr
            self.curr = self.curr.next
            yield j.data
            
    def __len__(self):
        return self.n
    
    def __str__(self):
        string =  "["
        for i in self.list:
            string = string + str(i) + "->"
        
        string += "]"
        return str(string)
    
    def __repr__(self):
        self.string =  "["
        for i in self.list:
            self.string = self.string + str(i) + "->"
        
        self.string += "]"
        return repr(self.string)

    def __setitem__(self, arg, item):
        try:
            self.list[arg] = item
            
        except IndexError:
            return "Subscript is out of range"
        
    def __getitem__(self, arg):
        try:
            if isinstance(arg, int):
                return self.list[arg]
            elif isinstance(arg, slice):
                ACopy = copy.deepcopy(self)
                if arg.step == None:
                    ACopyList = ACopy.list[arg.start: arg.stop]
                    ListToLinkedList = LinkedList(ACopyList[0])
                    for i in ACopyList[1:]:
                        ListToLinkedList.append(i)
                    return ListToLinkedList
                if arg.step > 0:
                    ACopyList = ACopy.list[arg.start: arg.stop: arg.step]
                    ListToLinkedList = LinkedList(ACopyList[0])
                    for i in ACopyList[1:]:
                        ListToLinkedList.append(i)
                    return ListToLinkedList
                else:
                    raise ValueError
        except IndexError:
            return "Subscript is out of range"
        except ValueError:
            return "The step shouldn't be negative since the list is forward-linked"
            
    def __add__(self, item):
        NodeWItem = Node(item)
        TheCopy = copy.deepcopy(self)
        TheCopy.append(NodeWItem)
        return TheCopy
# =============================================================================
#     def next(self):
# 
#         if self.curr == None:
#             self.curr = self.first
#             raise StopIteration
#           
#         else:
#             j = self.curr
#             self.curr = self.curr.next
#             return j.data
# =============================================================================
        
#%%

a = LinkedList(0);
a.append(1)
a.append(2)
 
print "40 points if this works"
for n in a:
    print n
 
print ""
 
print "10 points if this works"
for n in a:
    print n
     
print ""
     
print "15 points if both of these work"
for n in a:
    if n == 2: # if you wrote your code for n.data == 2, that's OK too
        break
    else:
        print n
  
print ""
        
for n in a:
    if n == 2: 
        break
    else:
        print n
 
print ""
 
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)
a.append(8)
 
print ""
 
print "5 points each"
print len(a)
print str(a)
print repr(a)
 
print ""
 
print "5 points each. That is, 10 points if the output of the next line is correct"
a[5] = 20
print a[5]
 
print ""
 
print "10 points for correct operation of +"
a+9 # doesn't modify a
print a
 
print ""
 
a = a+9 # appends 9 to a
print a
     
print ""
 
print "10 bonus points if all the following work"
print a[1:5]
print a[1:]
print a[:5]
print a[1::2]
print a[::]
 
print ""
print "-----"
print ""
print "Example output:"
print """
40 points if this works
0
1
2
 
10 points if this works
0
1
2
 
15 points if both of these work
0
1
 
0
1
 
 
5 points each
9
[0->1->2->3->4->5->6->7->8->]
'[0->1->2->3->4->5->6->7->8->]'
 
5 points each. That is, 10 points if the output of the next line is correct
20
 
10 points for correct operation of +
[0->1->2->3->4->20->6->7->8->]
 
[0->1->2->3->4->20->6->7->8->9->]
 
10 bonus points if all the following work
[1->2->3->4->]
[1->2->3->4->20->6->7->8->9->]
[0->1->2->3->4->]
[1->3->20->7->9->]
[0->1->2->3->4->20->6->7->8->9->]
"""