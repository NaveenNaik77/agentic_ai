import re

# ---------------------------
# CALCULATOR TOOL
# ---------------------------

def calculator_tool(user_input):
    try:
        expression = re.sub(r'[^0-9\+\-\*/\.\(\) ]', '', user_input)
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid calculation."

# ---------------------------
# WEATHER TOOL (MOCK)
# ---------------------------

def weather_tool(user_input):
    return "Weather today is sunny, 30°C."

# ---------------------------
# TEXT SUMMARIZER TOOL (IMPROVED)
# ---------------------------

def summarizer_tool(user_input):
    # Extract text after "summarize"
    text = user_input.lower().replace("summarize", "").strip()

    if not text:
        return "Please provide text to summarize."

    # Split into sentences
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return "Invalid input."

    # Remove very short sentences (less meaningful)
    sentences = [s for s in sentences if len(s.split()) > 3]

    if not sentences:
        return "Text too short to summarize."

    # Rank sentences by length (simple importance heuristic)
    sentences.sort(key=lambda s: len(s.split()), reverse=True)

    # Take top 1 or 2 sentences (real summarization effect)
    top_sentences = sentences[:2]

    summary = ". ".join(top_sentences)

    return f"Summary: {summary}."