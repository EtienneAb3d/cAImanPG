from Agent import Agent
from AgentExpert import AgentExpert

class AgentSupport(Agent):
    """
    The client Support agent is dedicated to a polite communication using very easy to understand explanations. 
    This agent is analyzing the client request to identify possible technical problems he encounters with his computer 
    that can be mixed with not technical contents. 
    It also extracts some informations like the client name. For each technical problem it sends a request 
    to the second agent to get a procedure to solve the problem.
    """
    def __init__(self):
        super().__init__(system_prompt = """
You are a client support agent in charge of answering computer technical questions.
If the client is providing with his/her name, use it to build a polite answer.
If there is one or several technical problem described (trouble like speed, freeze, not starting, crash, etc), for each technical problem described, do not build a response by yourself, but build a proper question to ask to a technical expert using the available function.
Using the technical expert responses, build a very comprehensive response with using simple terms and formulation, knowing the client is certainly not very comfortable with technical explanations.
If the client message contains very ordinary everyday life problem descriptions or questions (cooking, time management, transportation, etc), build a small response for it.
If the client message contains hard or sensitive problem descriptions or questions (politics, sex, religion, health, programming, etc) kindly explain you are only answering technical computer questions and provide some suggestions about persons to contact for these cases.
If the client content do not mention any computer technical problem or trouble invite to give more explanation related to a technical problem.
""")

        self.available_functions: list = [
            {
                "name": "ask_expert",
                "description": "Send a question in natural language to a computer technical expert.",
                "question_description":"A single technical question the expert should answer.",
            },
        ]

    def chat_assistant(self, question: str) -> str:
        answer = super().chat_assistant(
            question=question, 
            available_functions=self.available_functions,
            )
        
        if answer is not None:
            return answer+"\n\n"

        return "Internal trouble: no answer produced."
    
    def tool_call(self,function_name:str,question:str) -> str:
        if function_name == "ask_expert":
            test_agent = AgentExpert()
            print(f"Question from Support Agent to Expert Agent: {question}")
            answer = test_agent.chat_assistant(question)
            print(answer)
        return answer
