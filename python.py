# test.py

def add(a, b):
    """Function to add two numbers"""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers"""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b

def divide(a, b):
    """Function to divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Example usage
if __name__ == "__main__":
    x = 10
    y = 5
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
