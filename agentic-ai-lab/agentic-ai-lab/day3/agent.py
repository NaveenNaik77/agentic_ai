from tools import calculator_tool, weather_tool, summarizer_tool
from logger import log_interaction
from llm import CustomLLM

# Initialize LangChain LLM
llm = CustomLLM()

# ---------------------------
# LLM DECISION FUNCTION
# ---------------------------

def decide_tool_with_llm(user_input):
    prompt = f"""
You are an AI agent. Choose the correct tool:

Options:
- calculator
- weather
- summarizer

User input: {user_input}

Answer with only one word.
"""

    decision = llm.invoke(prompt).strip().lower()
    return decision

# ---------------------------
# PROCESS INPUT
# ---------------------------

def process_input(user_input):
    tool = decide_tool_with_llm(user_input)

    if "calculator" in tool:
        output = calculator_tool(user_input)

    elif "weather" in tool:
        output = weather_tool(user_input)

    elif "summarizer" in tool:
        output = summarizer_tool(user_input)

    else:
        output = "Sorry, I couldn't determine the correct tool."

    log_interaction(user_input, tool, output)

    return output

# ---------------------------
# MAIN LOOP
# ---------------------------

if __name__ == "__main__":
    print("LangChain LLM-Based Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        response = process_input(user_input)
        print("Agent:", response)