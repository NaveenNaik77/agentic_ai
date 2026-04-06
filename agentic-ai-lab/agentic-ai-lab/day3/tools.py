import re

def calculator_tool(user_input):
    try:
        expression = re.sub(r'[^0-9\+\-\*/\.\(\) ]', '', user_input)
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid calculation."

def weather_tool(user_input):
    return "Weather today is sunny, 30°C."

def summarizer_tool(user_input):
    text = user_input.lower().replace("summarize", "").strip()

    if not text:
        return "Please provide text to summarize."

    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return "Invalid input."

    sentences = [s for s in sentences if len(s.split()) > 3]

    if not sentences:
        return "Text too short to summarize."

    sentences.sort(key=lambda s: len(s.split()), reverse=True)
    summary = ". ".join(sentences[:2])

    return f"Summary: {summary}."