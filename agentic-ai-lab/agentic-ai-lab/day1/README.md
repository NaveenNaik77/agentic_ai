# Assignment 1: Rule-Based AI Agent

## Objective

The objective of this assignment is to build a simple rule-based AI agent that can:
- Take user input
- Identify user intent using keyword matching
- Perform appropriate actions

---

## Agent Architecture

The agent follows a structured pipeline:

Input → Decision → Action → Output

---

## Implementation Details

### 1. Input Handler
- Accepts user input from the command line
- Runs continuously until the user types `exit`

### 2. Decision Logic
- Uses keyword matching and operator detection
- Identifies intent such as:
  - Greeting
  - Date request
  - Mathematical calculation

### 3. Action Execution
- Executes functions based on detected intent:
  - `calculate()` → evaluates math expressions
  - `get_date()` → returns current date
  - `greet()` → returns greeting message
  - `unknown()` → handles unsupported queries

---

## Features

- Supports basic and complex mathematical expressions
- Handles expressions with brackets and decimals
- Detects intent without strict keyword dependency
- Modular and clean code structure
- Error handling for invalid inputs

---

## Example Inputs

- hello  
- hi  
- date  
- what is the date today  
- 2+3  
- (8*6)/4  
- calculate 10 + 5  

---

## Sample Output
You: hello
Agent: Hello! How can I help you?

You: (8*6)/4
Agent: Result: 12.0

You: date
Agent: Today's date is 2026-04-04

You: hello
Agent: Hello! How can I help you?

You: (8*6)/4
Agent: Result: 12.0

You: date
Agent: Today's date is 2026-04-04