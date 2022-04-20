# python implementation of single linked list 

from itertools import count


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('Empty linkedlist')
            return
        
        sll = ''
        itr = self.head
        while itr:
            sll += str(itr.data) + '-->'
            itr = itr.next
        print(sll)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
            return 
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data)
                break
            itr = itr.next


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index > self.get_length() or index < 0:
            raise Exception('Invalid Index!')
        
        if index == 0:
            self.insert_at_beginning(data, self.head)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == (index - 1):
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index >= self.get_length() or index < 0:
            raise Exception('Invalid Index!')
        
        if index == 0:
            self.head = self.head.next
            return 
        count = 0
        itr = self.head
        while itr:
            if count == (index - 1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break
            itr = itr.next
            count += 1
        else:
            raise Exception(f'Value - {data} not Found!')

if __name__ == '__main__':
    # l = LinkedList()
    # l.insert_at_beginning(1)
    # l.insert_at_beginning(2)
    # l.insert_at_beginning(3)
    # l.insert_at_beginning(4)
    # l.insert_at_beginning(5)
    # l.insert_at_end(10)
    # l.print()
    # l.get_length()
    # l.remove_by_value(10)
    # l.print()
    # l.get_length()
    # g = LinkedList()
    # g.insert_values(['1','2','3','4','5'])
    # g.print()
    # g.get_length()
    # g.remove_by_value('5')
    # g.print()
    # g.get_length()

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

