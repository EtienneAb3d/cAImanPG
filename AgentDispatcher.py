import json
import re
from Agent import Agent
from AgentComputer import AgentComputer
from AgentCooking import AgentCooking

class AgentDispatcher(Agent):
    """
    The Cooking agent is analyzing the request from the first agent to build cooking suggestions.
    """
    def __init__(self):
        self.domains = ["Cooking", "Computer", "Other"]
        system_prompt = """
Write a JSON string listing each problem or question identified in the user's message.
Only one line per question or problem identified.
Format to be respected:
[
    [“Domain (keyword from list)”, “Question (formulate the question for a domain expert independently of other questions)”],
    [“Domain (keyword from list)”, “Question (formulate the question for a domain expert independently of other questions)”],
]
Here are the domains you can refer to, without necessarily taking them all, but without inventing other names:
DOMAINS.
If no problem or question is clearly identified in the user's message (greeting, ordinary discussion, etc), or no domain is clearly targeted in the user's message, or if the user's message is too confusing, simple answer "BlaBla".
"""
        system_prompt = re.sub(r"DOMAIN",", ".join(self.domains),system_prompt)
        super().__init__(system_prompt=system_prompt)

    def dispatch(self, user_question:str) -> list:
        """
        Maps a user's natural language questions to be sent to an Expert.
        :param user_question: str, list of domain/question pairs. May be an empty list.
        :return: list
        """
        try:
            answer = super().chat_assistant(
                question=user_question,
                )
            dispatch = []
            print(f"Dispatcher:\n{answer}")
            if answer == "BlaBla":
                return dispatch
            try:
                qas = json.loads(answer)
                for index,item in enumerate(qas):
                    domain = item[0]
                    if domain == "Other" or domain not in self.domains:
                        # Ignore
                        continue

                    agent = None
                    if domain == "Cooking":
                        agent = AgentCooking()
                    if domain == "Computer":
                        agent = AgentComputer()

                    if agent is None:
                        continue

                    question = item[1]
                    print(f"\n\n##### Question from Dispatcher Agent to {domain} Agent:\n{question}\n")
                    tip = agent.chat_assistant(question)
                    print(tip)

                    dispatch.append([domain,tip])

                print("\n#### All dispatches done ####\n")
            except Exception as e:
                print(f"JSON error '{str(e)}' in '{answer}'")
            return dispatch
        except Exception as e:
            print(f"Internal error '{str(e)}' for '{user_question}'")
        return []

