from Node import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def insert( self, val ):
        newNode = Node( val )
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
    
    def remove( self ):
        if self.top != None:
            current = self.top
            self.top = current.next
            current.next = None
    
    def isEmpty( self ):
        if self.top == None:
            return True
        else:
            return False

    def printStack( self ):
        current = self.top
        while current != None:
            print( current.val )
            current = current.next