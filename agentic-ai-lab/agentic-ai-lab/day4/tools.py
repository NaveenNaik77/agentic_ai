import re

# ---------------------------
# NUMBER EXTRACTION
# ---------------------------
def extract_numbers(text):
    return list(map(int, re.findall(r'\d+', text)))

# ---------------------------
# CALCULATOR
# ---------------------------
def calculator_tool(text):
    try:
        expression = re.sub(r'[^0-9\+\-\*/\.\(\) ]', '', text)
        return eval(expression)
    except:
        return "Invalid calculation"

# ---------------------------
# AVERAGE
# ---------------------------
def calculate_average(numbers):
    if not numbers:
        return "No numbers found"
    return sum(numbers) / len(numbers)

# ---------------------------
# WEATHER
# ---------------------------
def weather_tool(_):
    return "Weather today is sunny, 30°C."

# ---------------------------
# SUMMARIZER
# ---------------------------
def summarizer_tool(text):
    return f"Summary: {text}"