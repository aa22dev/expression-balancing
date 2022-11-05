# Expression balancing using stack
from collections import deque # importing double ended queue from collections library

exp = input("Enter any equation: ") # take input of expression from user
stack = deque() # initialize stack using double ended queue
dic = {
    '{': '}',
    '[': ']',
    '(': ')'
} # dictionary to store opening brackets as key and closing brackets as value
result = 1 # bool variable acting as a flag
for i in exp: # loop through every character of expression
    if i in dic.keys(): # check if character is opening bracket
        stack.append(i) # append it to stack
    elif i in dic.values(): # check if character is closing bracket
        if not stack: # if stack is empty
            result = 0 # set flag to 0
            break # break loop
        elif i not in dic[stack[-1]]: # if top of stack doesn't contain corresponding opening bracket for closing bracket entered
            result = 0 # set flag to 0
            break # break loop
        stack.pop() # pop the value from top of stack
if result: # if flag is 1
    print("Valid Expression!") # print valid expression
else:
    print("Invalid Expression!") # print invalid expression
