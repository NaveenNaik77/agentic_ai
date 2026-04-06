def create_plan(user_input):
    user_input = user_input.lower()
    plan = []

    # Step detection (multi-intent)

    if "average" in user_input:
        plan.append("extract_numbers")
        plan.append("calculate_average")

    # Calculator (but not when average already handles it)
    elif any(op in user_input for op in ['+', '-', '*', '/']):
        plan.append("calculate_expression")

    if "weather" in user_input:
        plan.append("weather")

    if "summarize" in user_input:
        plan.append("summarize")

    return plan