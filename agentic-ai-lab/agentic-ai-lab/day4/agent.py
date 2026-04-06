from tools import (
    extract_numbers,
    calculate_average,
    calculator_tool,
    weather_tool,
    summarizer_tool
)

from planner import create_plan

def execute_plan(user_input):
    plan = create_plan(user_input)

    print("\n--- EXECUTION PLAN ---")
    print(plan)
    print("----------------------\n")

    data = user_input
    numbers = None
    result = None

    for step in plan:

        if step == "extract_numbers":
            numbers = extract_numbers(data)
            print(f"Step: Extract Numbers → {numbers}")

        elif step == "calculate_average":
            result = calculate_average(numbers)
            print(f"Step: Calculate Average → {result}")

        elif step == "calculate_expression":
            result = calculator_tool(data)
            print(f"Step: Calculate Expression → {result}")

        elif step == "weather":
            result = weather_tool(data)
            print(f"Step: Weather → {result}")

        elif step == "summarize":
            result = summarizer_tool(result)
            print(f"Step: Summarize → {result}")

    return result

# ---------------------------
# MAIN LOOP
# ---------------------------
if __name__ == "__main__":
    print("Multi-Step Agent (Generalized) (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye!")
            break

        output = execute_plan(user_input)
        print("\nFinal Output:", output)