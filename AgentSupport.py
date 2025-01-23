from openai import OpenAI
from openai.types.chat.chat_completion_tool_param import ChatCompletionToolParam
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionMessage,
    ChatCompletionToolMessageParam,
)

from Utils import load_api_key
from AgentExpert import AgentExpert

class AgentSupport:
    system_prompt = """
You are a client support agent in charge of answering computer technical questions.
If the client is providing with his/her name, use it to build a polite answer.
If there is on or several technical problem described (trouble like speed, freeze, not starting, crash, etc), for each technical problem described, do not build a response by yourself, but build a proper question to ask to a technical expert using the available function.
Using the technical expert responses, build a very comprehensive response with using simple terms and formulation, knowing the client is certainly not very comfortable with technical explanations.
If the client content do not mention any computer technical problem or trouble, kindly explain you are only answering technical questions, and invite to give more explanation related to a technical problem.
For the content part of the client request that do not involve any technical problem, build a kind message to show your empathy.
"""

    available_functions: list[ChatCompletionToolParam] = [
        {
            "type": "function",
            "function": {
                "name": "ask_expert",
                "description": "Send a question in natural language to a computer technical expert.",
                "parameters": {"type": "object", "properties": {
                    "question" : {
                        "type":"string",
                        "description":"A single technical question the expert should answer.",
                        },
                    }, "required": ["question"]},
            },
        },
    ]

    def __init__(self):
        self.openai = OpenAI(api_key=load_api_key(file_path='openai_api_key.txt'))

    async def start_chat(self, question: str):
        answer: str | ChatCompletionMessage | None = None

        messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": question},
        ]

        msgs = []

        while True:
            answer = self.chat_assistant(messages, self.available_functions)
            messages.append(answer)  # type: ignore
            if answer.content is not None:
                yield answer.content+"\n\n"
            if answer.tool_calls and len(answer.tool_calls) > 0:
                result = []
                for tool_call in answer.tool_calls:
                    if tool_call.function.name == "ask_expert":
                        test_agent = AgentExpert()
                        print(f"Question from Support Agent to Expert Agent: {str(tool_call.function.arguments)}")
                        answer = test_agent.get_technical_answer(tool_call.function.arguments)
                        print(answer)
                        tool_result: ChatCompletionToolMessageParam = {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "content": answer,
                        }
                        result.append(tool_result)
                messages.extend(result)
            else:
                break
    
    def chat_assistant(
        self,
        messages: list[ChatCompletionMessageParam],
        descriptions: list[ChatCompletionToolParam],
    ) -> ChatCompletionMessage:
        response = self.openai.chat.completions.create(
            model="gpt-4",
            messages=messages,
            tools=descriptions,
            temperature=0,
        )

        assistant_answer = response.choices[0].message

        return assistant_answer
