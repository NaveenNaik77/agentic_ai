from langchain_core.language_models.llms import LLM

class CustomLLM(LLM):
    def _call(self, prompt, stop=None):
        # Extract ONLY user input
        user_input = prompt.split("User input:")[-1].strip().lower()

        # 1. Summarizer
        if "summarize" in user_input:
            return "summarizer"

        # 2. Weather
        elif "weather" in user_input:
            return "weather"

        # 3. Calculator (ONLY if numbers + operators exist)
        elif any(op in user_input for op in ['+', '*', '/']) or \
             any(char.isdigit() for char in user_input):
            return "calculator"

        else:
            return "unknown"

    @property
    def _llm_type(self):
        return "custom_llm"