def is_valid_parentheses(s):
    stack = []
   
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False  
            stack.pop() 

    return not stack  

expression = input("Enter the expression with brackets: ")

if is_valid_parentheses(expression):
    print("The parentheses are valid.")
else:
    print("The parentheses are not valid.")