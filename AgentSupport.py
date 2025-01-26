from Agent import Agent
from AgentComputer import AgentComputer
from AgentCooking import AgentCooking

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
You are a client support agent in charge of answering client questions and suggest solutions.
If the client is providing with his/her name, use it to build a polite answer.
For each problem or question in the client request, use the available function to identify an expert on the related subject.
If an expert exists for the subject do not build a response by yourself, but build a proper question to ask to the identified expert using the available function.
Using the technical expert responses, build a very comprehensive response with using simple terms and formulation, knowing the client is certainly not very comfortable with technical explanations.
If there is no expert identified on the subject and the client message contains very ordinary everyday life problem descriptions or questions (cooking, time management, transportation, etc), build a small response for it by your own.
If the client message contains hard or sensitive problem descriptions or questions (politics, sex, religion, health, programming, etc) kindly explain you are not competent for such a subject and provide some suggestions about persons to contact for these cases.
If the client content do not mention any problem or trouble kindly invite to give more explanation related to a technical problem.                      
""")

        self.available_functions: list = [
            {
                "name": "ask_computer_expert",
                "description": "Send a question in natural language to a computer expert.",
                "question_description":"A single question the expert should answer on computer subjects.",
            },
            {
                "name": "ask_cooking_expert",
                "description": "Send a question in natural language to a cooking expert.",
                "question_description":"A single question the expert should answer on cooking subjects.",
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
        print(f"Question from Support Agent to {function_name} Agent: {question}")
        if function_name == "ask_computer_expert":
            test_agent = AgentComputer()
        if function_name == "ask_cooking_expert":
            test_agent = AgentCooking()
        answer = "No answer provided." if not test_agent else test_agent.chat_assistant(question)
        print(answer)
        return answer
