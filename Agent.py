from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from Config import get_model
import re

class Agent:
    """
    The Agent superclass is managing the ChatGPT completion requests logic.
    """
    def __init__(self,system_prompt:str):
        self.model_familly,self.model,self.url,self.api_key = get_model()
        self.openai = OpenAI(base_url=self.url, api_key=self.api_key)
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
                # Remove DeepSeek <think>
                filtered = re.sub(r"<think>.*</think>\n*","",answer.content, flags=re.DOTALL).strip()
                return filtered
    
    def tool_call(self,function_name:str,question:str) -> str:
        return None

