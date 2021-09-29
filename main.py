from Stack import Stack

numsStack = Stack()

numsStack.insert( 10 )
numsStack.insert( 8 )
numsStack.insert( 6 )
numsStack.insert( 4 )
numsStack.insert( 2 )

numsStack.remove()
numsStack.remove()



def validateExpression( formula ):
    parenthesisStack = Stack()

    for current in formula:
        if current == "(" or current == "[" or current == "{":
            parenthesisStack.insert( current )
        if current == ")":
            if parenthesisStack.isEmpty():
                return False
            else:
                if parenthesisStack.top.val == "(":
                    parenthesisStack.remove()
                else:
                    return False
        if current == "]":
            if parenthesisStack.isEmpty():
                return False
            else:
                if parenthesisStack.top.val == "[":
                    parenthesisStack.remove()
                else:
                    return False
        if current == "}":
            if parenthesisStack.isEmpty():
                return False
            else:
                if parenthesisStack.top.val == "{":
                    parenthesisStack.remove()
                else:
                    return False

    if parenthesisStack.isEmpty():
        return True
    else:
        return False
    

result = validateExpression( "(b - a) * ) c / 4 ( * (c + b)" )
print( result )

# Write a function called validateExpression.
# This function receives a string as an argument
# You must validate that the string has implemented parentesis
# correctly in a formula

# BONUS, validate that it has square brackets and curly braces implemented correctly as well

# x*(x+z) + x/(y-z) + d should return true
# t – (s-k + x should return false
# ((x + y) * (x + 7)) / )y( should return false
# (((x+z)/(x*y)) + 4 ) should return true
# x + y / ) z + 1 ( * (r - z) should return false
# (b - a) * ) c / 4 ( * (c + b) should return false
# (b - a) * ) c / 4 ( * (c + b)) should return false