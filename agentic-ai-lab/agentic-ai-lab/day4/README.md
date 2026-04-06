# Assignment 4: Multi-Step Agent (Planning-Based Agent)

## Objective

The objective of this assignment is to design an AI agent capable of solving complex tasks by breaking them into multiple steps and executing them sequentially.

---

## Architecture

The agent follows a planning-based pipeline:

User Input → Planner → Execution Steps → Final Output

---

## Implementation Details

### 1. Planner (planner.py)

- Responsible for analyzing user input
- Breaks the task into multiple steps
- Generates an execution plan dynamically

Example:
Input:  
"Find the average of 5, 10, 15 and summarize"

Plan:
- extract_numbers  
- calculate_average  
- summarize  

---

### 2. Tools (tools.py)

The agent uses multiple tools:

- **extract_numbers()**
  - Extracts numbers from input

- **calculate_average()**
  - Computes average of numbers

- **calculator_tool()**
  - Performs arithmetic operations

- **weather_tool()**
  - Returns weather information (mock)

- **summarizer_tool()**
  - Converts result into readable summary

---

### 3. Agent (agent.py)

- Executes steps returned by the planner
- Maintains intermediate results
- Prints each step output
- Produces final result

---

## Features

- Multi-step reasoning
- Dynamic planning based on user input
- Supports multiple tools in a single query
- Sequential execution of tasks
- Displays intermediate outputs
- Modular and extensible design

---

## Example Queries

- Find the average of 5, 10, 15 and summarize  
- What is (8*6)/4  
- Calculate 10+5 and summarize  
- weather today  
- Find average of 10, 20, 30 and summarize and tell weather  

---

## Sample Execution



---

## Learning Outcomes

- Task decomposition
- Planning-based agent design
- Sequential reasoning
- Multi-step execution
- Tool orchestration

---

## Limitations

- Planning is rule-based (not LLM-driven)
- Limited understanding of complex natural language
- No real-time external API integration

---

## Future Improvements

- LLM-based planning for dynamic reasoning
- Integration with external APIs (weather, search)
- Memory for multi-turn conversations
- Advanced summarization techniques

---

## Conclusion

This assignment demonstrates how an AI agent can solve complex problems by breaking them into smaller steps and executing them sequentially, which is a key concept in modern Agentic AI systems.