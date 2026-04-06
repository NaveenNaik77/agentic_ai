from tools import calculator_tool, weather_tool, summarizer_tool

# ---------------------------
# DECISION LOGIC
# ---------------------------

def decide_tool(user_input):
    user_input = user_input.lower()

    if any(op in user_input for op in ['+', '-', '*', '/']):
        return "calculator"

    elif "weather" in user_input:
        return "weather"

    elif "summarize" in user_input:
        return "summarizer"

    else:
        return "unknown"

# ---------------------------
# TOOL EXECUTION
# ---------------------------

def process_input(user_input):
    tool = decide_tool(user_input)

    if tool == "calculator":
        return calculator_tool(user_input)

    elif tool == "weather":
        return weather_tool(user_input)

    elif tool == "summarizer":
        return summarizer_tool(user_input)

    else:
        return "Sorry, I don't understand the request."

# ---------------------------
# MAIN LOOP
# ---------------------------

if __name__ == "__main__":
    print("Tool-Based AI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        response = process_input(user_input)
        print("Agent:", response)