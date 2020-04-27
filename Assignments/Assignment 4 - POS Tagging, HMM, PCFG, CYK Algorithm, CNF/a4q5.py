#!/local/bin/python3
import sys


class Node:
    def __init__(self):
        self.character = '('
        self.count = 0


def check_cnf_validity(text):
    stack = []
    valid = True
    txt_arr = text.split(' ')
    arr = []
    for i in txt_arr:
        for j in i:
            arr.append(j)

    for word in arr:
        if word == '(':
            if not stack:
                stack.append(Node())
            else:
                stack[-1].count += 1
                stack.append(Node())

        elif word == ')':
            if stack[-1].count > 2 or stack[-1].count == 1:
                valid = False
                stack = []
                break
            else:
                stack.pop()
        else:
            pass

    return valid


txt = sys.stdin.read()

validity = check_cnf_validity(txt)
if validity:
    print("\nValid CNF trees.\n")
else:
    print("\nInvalid CNF trees.\n")
