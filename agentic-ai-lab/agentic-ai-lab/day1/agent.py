import datetime
import re

# ---------------------------
# ACTION FUNCTIONS
# ---------------------------

def calculate(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception:
        return "Invalid calculation. Please enter a valid math expression."

def get_date():
    today = datetime.date.today()
    return f"Today's date is {today}"

def greet():
    return "Hello! How can I help you?"

def unknown():
    return "Sorry, I didn't understand that."

# ---------------------------
# DECISION LOGIC
# ---------------------------

def decide_intent(user_input):
    user_input = user_input.lower()

    # Detect math expressions
    if any(op in user_input for op in ['+', '-', '*', '/']):
        return "calculator"

    elif "date" in user_input or "day" in user_input:
        return "date"

    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        return "greeting"

    else:
        return "unknown"

# ---------------------------
# INPUT PROCESSING
# ---------------------------

def extract_expression(user_input):
    """
    Extracts a valid mathematical expression from input.
    Supports brackets and multiple operations.
    """
    # Remove unwanted characters except math symbols
    expression = re.sub(r'[^0-9\+\-\*/\.\(\) ]', '', user_input)
    return expression.strip()

# ---------------------------
# MAIN PROCESS FUNCTION
# ---------------------------

def process_input(user_input):
    intent = decide_intent(user_input)

    if intent == "calculator":
        expression = extract_expression(user_input)
        if expression:
            return calculate(expression)
        else:
            return "Please provide a valid math expression."

    elif intent == "date":
        return get_date()

    elif intent == "greeting":
        return greet()

    else:
        return unknown()

# ---------------------------
# MAIN LOOP
# ---------------------------

if __name__ == "__main__":
    print("Simple AI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        response = process_input(user_input)
        print("Agent:", response)