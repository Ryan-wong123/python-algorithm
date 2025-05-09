from qn_1_stack import Stack

def is_balanced(expression):
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching[char]:
                return False

    return stack.is_empty()

expr1 = "{[()()]}"      # ✅ Balanced
expr2 = "{[(])}"        # ❌ Not balanced
expr3 = "([{}]){}"      # ✅ Balanced
expr4 = "((("           # ❌ Not balanced

for expr in [expr1, expr2, expr3, expr4]:
    print(f"{expr} → {'Balanced' if is_balanced(expr) else 'Not Balanced'}")
