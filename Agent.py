from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from Utils import load_api_key
import json

# May be "Mistral or "ChatGPT"
llm = "Mistral"

class Agent:
    """
    The Agent superclass is managing the ChatGPT completion requests logic.
    """
    def __init__(self,system_prompt:str):
        if llm == "Mistral":
            self.model = "mistralai/Mistral-7B-Instruct-v0.3"
            self.openai = OpenAI(base_url='http://localhost:8001/v1', api_key='cubAIx')
        else:
            self.model = "gpt-4"
            self.api_key = load_api_key('openai_api_key.txt')
            self.openai = OpenAI(api_key=self.api_key)
        self.system_prompt: str = system_prompt
        self.messages: list[ChatCompletionMessageParam] = []

    def chat_assistant(
        self,
        question: str,
    ) -> str:
        self.messages.extend([
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": question},
        ])

        answer = None

        while True:
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=0.1,
            )

            answer = response.choices[0].message

            self.messages.append(answer)

            if answer.content is not None:
                return answer.content
    
    def tool_call(self,function_name:str,question:str) -> str:
        return None

