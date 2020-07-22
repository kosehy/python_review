"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
print(myStack.peek())

def is_paren_balanced(paren_string):
    s =Stack()
    is_balanced = True
    
    if paren_string == '':
        is_balanced = False
        return is_balanced
    for i in paren_string:
        if i == '{' or i == '[' or i == '(':
            s.push(i)
        else:
            if i == '}':
                if s.peek() == '{':
                    s.pop()
                else:
                    is_balanced = False
                break
            elif i == ']':
                if s.peek() == '[':
                    s.pop()
                else:
                    is_balanced = False
                break
            elif i == ')':
                if s.peek() == '(':
                    s.pop()
                else:
                    is_balanced = False
                break
            else:
                is_balanced = False
    return is_balanced

test = "[][][]*"
is_paren_balanced(test)