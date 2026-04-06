# Assignment 2: Tool-Based AI Agent

## Objective

To build an AI agent that can use external tools to perform tasks.

---

## Architecture

User Input → Agent → Tool Selection → Tool Execution → Output

---

## Tools Implemented

### 1. Calculator Tool
- Performs arithmetic operations
- Supports complex expressions

### 2. Weather Tool
- Returns mock weather data

### 3. Text Summarizer Tool
- Generates a short summary of input text

---

## Implementation

### tools.py
Contains all tool functions:
- calculator_tool()
- weather_tool()
- summarizer_tool()

### agent.py
- Decides which tool to use
- Calls appropriate tool
- Returns result

---

## Features

- Modular design (separate tools and agent)
- Dynamic tool selection
- Handles multiple types of inputs

---

## Example Inputs

- 2+3
- weather today
- summarize AI is changing the world

---

## Learning Outcomes

- Tool abstraction
- Function-based modular design
- Agent decision-making process

---

## Limitations

- Uses keyword-based decision logic
- Weather data is mocked

---

## Future Improvements

- Integrate real APIs
- Use LLM for smarter tool selection

## Outputs
summarize Machine learning is a subset of AI. It allows systems to learn from data. It is widely used in recommendation systems and fraud detection.

summarize AI helps automate tasks. It improves efficiency. It is useful.

summarize Artificial Intelligence is transforming industries across the world. It helps automate repetitive tasks and improves efficiency. Many companies are investing heavily in AI technologies. However, it also raises ethical concerns about job loss and privacy.