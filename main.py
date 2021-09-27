from Stack import Stack

numsStack = Stack()

numsStack.insert( 10 )
numsStack.insert( 8 )
numsStack.insert( 6 )
numsStack.insert( 4 )
numsStack.insert( 2 )

numsStack.printStack()

numsStack.remove()
numsStack.remove()

print( "-------" )
numsStack.printStack()
