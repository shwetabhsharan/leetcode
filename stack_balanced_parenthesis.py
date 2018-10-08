"""
Stack implementation to check if the parenthesis is balanced or not.
Logic: This function, is_balanced, returns a boolean result as to
        whether the string of parentheses is balanced. If the current
        symbol is (, then it's pushed on the stack. If it is ) we
        attempt to pop from the stack. If the stack is empty at that
        point, we know that the parenthesis string is imbalanced with
        too many closing parens. Finally, as long as the expression
        is balanced and the stack has been completely cleaned off,
        the string represents a correctly balanced sequence of
        parentheses.
"""

parenthesis = "("

def is_balanced(parenthesis_string):
    stack = []
    for paren in parenthesis_string:
        if paren == parenthesis:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0

print is_balanced("(())(()))")