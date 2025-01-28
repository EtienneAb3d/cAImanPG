from Agent import Agent
from AgentDispatcher import AgentDispatcher

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
Always answer in the original client language (French if the client message is in French).
If the client is providing with his/her name, use it to build a polite answer.
For each problem or question in the client request, use the possible provided expert tips on the related subject that was added to his message.
Inspired by the expert tips, build a very comprehensive answer with using simple terms and formulation, knowing the client is certainly not very comfortable with technical explanations.
Be aware that the client is not informed of expert tips added to his message: your answer must be understandable without knowing the expert tips.
If there is no expert tips identified on the subject and the client message contains very ordinary everyday life problem descriptions or questions (cooking, time management, transportation, etc), build a small response for it by your own.
If the client message contains hard or sensitive problem descriptions or questions (politics, sex, religion, health, programming, etc) kindly explain you are not competent for such a subject and provide some suggestions about persons to contact for these cases.
If the client content do not mention any problem or trouble, write a very short answer of 2 sentences that kindly invite to give more explanation related to a technical problem.
""")

    def chat_assistant(self, user_question: str) -> str:
        q_lines = []
        q_lines.append("*** Client Question ***")
        q_lines.append(user_question)

        dispatcher = AgentDispatcher()
        dispatch = dispatcher.dispatch(user_question=user_question)
        if dispatch:
            for disp in dispatch:
                q_lines.append(f"\n*** {disp[0]} Expert Tip***")
                q_lines.append(disp[1])
 
        answer = super().chat_assistant(question="\n".join(q_lines))
        
        if answer is not None:
            return answer+"\n\n"

        return "Internal trouble: no answer produced."
    
