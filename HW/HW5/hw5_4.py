import re

def is_valid_expression(expression):
    # Check for unsupported characters
    if not re.match(r'^[\d+\-*/() ]*$', expression):
        return False, "Unsupported character error: The expression contains characters other than integers, addition, subtraction, multiplication, division, and parentheses."
    # Check for unbalanced parentheses
    if expression.count('(') != expression.count(')'):
        return False, "Unbalanced parentheses error: Number of opening and closing parentheses is not equal."
    # Check for operand errors (e.g., "5 + * 3")
    if re.search(r'[*/+-]{2,}', expression.replace(' ', '')):
        return False, "Operand error: Missing an operand before or after an operator."
    return True, ""

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Division by zero error: Division by zero in the expression."
    except SyntaxError:
        return "Operand error: Missing an operand before or after an operator."

def main():
    while True:
        expression = input("Enter an arithmetic expression (or 'q' to quit): ").strip()
        if expression.lower() == 'q':
            break
        
        is_valid, error_message = is_valid_expression(expression)
        if not is_valid:
            print(error_message)
            continue
        
        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()