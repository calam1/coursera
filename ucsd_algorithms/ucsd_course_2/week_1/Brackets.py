#python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    text = text.rstrip()
    close_open = {')':'(', ']':'[', '}':'{'}
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i,next))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                print(i+1)
                exit()

            open_value = opening_brackets_stack.pop()
            if open_value[1] != close_open.get(next):
                print(i+1)
                exit()

        #print('i {} length text {} length stack {}'.format(i, len(opening_brackets_stack), len(opening_brackets_stack)))
        if i+1 == len(text) and len(opening_brackets_stack) != 0:
            leftover = opening_brackets_stack.pop()
            print(leftover[0]+1)
            #print(i+1)
            exit()

    print('Success')
