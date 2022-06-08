def is_correct_bracket_seq(string):
    stack = []
    if string == '':
        return True
    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == '(' and stack[-1] != ')':
            return False
        elif char == ')' and len(stack) == 0:
            return False
        elif char == ')' and stack[-1] == '(':
            stack.pop()
        elif char == '}' and len(stack) == 0:
            return False
        elif char == '{' and stack[-1] != '}':
            return False
        elif char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == ']' and len(stack) == 0:
            return False
        elif char == '[' and stack[-1] != '[':
            return False
        elif char == ']' and stack[-1] == '[':
            stack.pop()
        elif (char == ')' or char == '}' or char == '}') and (stack == ''):
            return False
        else:
            return False
    if len(stack) != 0:
        return False
    else:
        return True


if __name__ == '__main__':
    string = input()
    print(is_correct_bracket_seq(string))