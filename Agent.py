import openai
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageToolCall,
    ChatCompletionToolMessageParam,
)
from Utils import load_api_key
import json

class Agent:
    """
    The Agent superclass is managing the ChatGPT logic: completion requests with or without functions.
    """
    def __init__(self,system_prompt:str):
        self.api_key = load_api_key('openai_api_key.txt')
        openai.api_key = self.api_key
        self.system_prompt: str = system_prompt
        self.messages: list[ChatCompletionMessageParam] = []

    def chat_assistant(
        self,
        question: str,
        available_functions: list = None,
    ) -> str:
        tools: list[ChatCompletionToolParam] = None if not available_functions else [
            {
                "type": "function",
                "function": {
                    "name": func["name"],
                    "description": func["description"],
                    "parameters": {"type": "object", "properties": {
                        "question" : {
                            "type":"string",
                            "description":func["question_description"],
                            },
                        },
                        "required": ["question"]},
                }
            }
            for func in available_functions]

        self.messages.extend([
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": question},
        ])

        answer = None

        while True:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=self.messages,
                tools=tools,
                temperature=0,
            )

            answer = response.choices[0].message

            self.messages.append(answer)

            if answer.content is not None:
                return answer.content
            if answer.tool_calls and len(answer.tool_calls) > 0:
                result = []
                for tool_call in answer.tool_calls:
                    question = json.loads(tool_call.function.arguments)["question"]
                    answer_tool = self.tool_call(tool_call.function.name,str(question))
                    tool_result: ChatCompletionToolMessageParam = {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_call.function.name,
                        "content": answer_tool,
                    }
                    result.append(tool_result)
                self.messages.extend(result)
    
    def tool_call(self,function_name:str,question:str) -> str:
        return None

