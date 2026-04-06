# Assignment 3: LLM-Based Agent

## Objective

The objective of this assignment is to integrate a language model (LLM) into an AI agent to improve decision-making.  
The agent uses an LLM to decide which tool to use based on user input.

---

## Architecture

The agent follows the pipeline:

User Input → LLM → Tool Selection → Tool Execution → Output

---

## Implementation Details

### 1. Tools

The agent supports the following tools:

- **Calculator Tool**
  - Performs arithmetic operations
  - Supports complex expressions

- **Weather Tool**
  - Returns mock weather data

- **Summarizer Tool**
  - Generates a concise summary of input text

All tools are implemented in `tools.py`.

---

### 2. LLM Integration

- Implemented using LangChain
- A custom LLM class (`CustomLLM`) is created
- The LLM processes prompts and decides which tool to use
- Uses prompt-based decision-making instead of rule-based logic

---

### 3. Agent Logic

- The agent sends user input to the LLM
- The LLM returns the appropriate tool name
- The agent executes the selected tool
- Output is returned to the user

---

### 4. Logging

The system logs every interaction:

- User Input  
- Selected Tool  
- Output  

This helps in debugging and understanding agent behavior.

---

## Features

- LLM-based decision making
- Modular design (separate tools, agent, and LLM)
- Prompt-based reasoning
- Lightweight implementation (no external API required)
- Real-time logging

---

## Example Inputs

- What is (8*6)/4?  
- weather today  
- summarize Artificial Intelligence is transforming industries...  

---

## Sample Output


---

## Test Cases Covered

- Arithmetic expressions (basic and complex)
- Weather-related queries
- Text summarization
- Mixed inputs
- Invalid inputs
- Unknown queries

---

## Learning Outcomes

- Understanding of LLM integration
- Prompt-based decision making
- Tool selection using AI
- Modular system design

---

## Limitations

- Uses a simulated LLM (no real API)
- Limited understanding of complex natural language
- Weather data is mocked

---

## Future Improvements

- Integration with real LLM APIs
- More advanced natural language understanding
- Support for additional tools
- Multi-step reasoning (next assignment)

---

## Note

LangChain is used to implement a custom LLM for tool selection.  
This approach simulates how an actual LLM would process prompts and make decisions, while remaining lightweight and compatible with limited system resources.