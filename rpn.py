import operator
import sys
stack = []

# Define the operations dictionary
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def display_stack(stack):
    if not stack:
        print("[]")
        return
    
    for i in range(len(stack)):
        if (i == 0) and (i == len(stack)- 1):  # unico elemento
            print(f"[{stack[i]}]")
            continue
        if (i != 0) and (i == len(stack)- 1):  # elemento al final del stack
            print(f" {stack[i]}]")
            continue
        if (i == 0) and (i != len(stack)- 1):  # elemento en el frente del stack
            print(f"[{stack[i]} ")
            continue
        if (i != 0) and (i != len(stack)- 1):  # elemento de en medio del stack
            print(f" {stack[i]} ")

def rpn_calculate():
    stack = []
    print("Interactive RPN Calculator")
    print("Enter numbers to push to the stack, or operators (+, -, *, /) to calculate.")
    print("Type 'q' or 'quit' to exit, 'c' or 'clear' to clear the stack, 'd' or 'drop' to remove the top item, 's' to view the stack.")
    display_stack(stack)

    while True:
        user_input = input("> ").split()
        for token in user_input:
            if token in ('q', 'quit'):
                print("Exiting calculator.")
                return

            if token in ('c', 'clear'):
                stack.clear()
                display_stack(stack)
                # print("Stack cleared.")
                continue
            
            if token in ('d', 'drop'):
                if stack:
                    droped_operand = stack.pop()
                    print(f"droped - > : {droped_operand}")
                else:
                    print("Error: stack is empty.")
                    display_stack(stack)
                continue

            if token in ('s', 'stack'):
                display_stack(stack)
                #print(f"Current stack: {stack}")
                continue

            try:
                # Try converting the token to a float
                number = float(token)
                stack.append(number)
            except ValueError:
                # If it's not a number, check if it's an operator
                if token in operators:
                    if len(stack) < 2:
                        print(f"Error: not enough operands for '{token}'.")
                        continue
                    # Pop two operands, perform the operation, and push the result back
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    try:
                        result = operators[token](operand1, operand2)
                        stack.append(result)
                    except ZeroDivisionError:
                        print("Error: division by zero.")
                        stack.append(operand1) # Push operands back to allow user correction
                        stack.append(operand2)
                else:
                    print(f"Error: unknown input '{token}'.")

        # Display the result of the last operation (top of stack) or the full stack
        if stack:
            # print(f"Stack top: {stack[-1]}")
            # Optional: print the full stack after each input line
            display_stack(stack)

if __name__ == "__main__":
    rpn_calculate()

