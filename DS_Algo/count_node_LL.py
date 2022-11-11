class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None
    
    def insert_beg(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node


    def count_node_LL(self):
        count=0
        current=self.head

        while(current):
            count +=1
            current=current.next
        return count

if __name__=='__main__':
    lst=Linked_list()
    lst.insert_beg(1)
    lst.insert_beg(2)
    lst.insert_beg(5)
    lst.insert_beg(9)
    lst.insert_beg(10)
    lst.insert_beg(3)

    print("the count of nodes is ",lst.count_node_LL())


    