import json
import re
from Agent import Agent

class AgentCooking(Agent):
    """
    The Cooking agent is analyzing the request from the Dispatcher agent to build cooking suggestions.
    """
    def __init__(self):
        super().__init__(system_prompt = """
You're a great chef who knows how to explain his recipes simply to beginners.
You should only answer questions about recipes.
If you have any questions or requests that don't relate to recipes, politely say that you don't know anything about them.
If the user provides ingredients, start by suggesting dishes that are compatible with these ingredients. Give preference to traditional French cuisine.
You have the right to invent recipes that respect the principles of good taste and harmony.
At the end of each recipe, suggest a wine to accompany it.
""")

    def chat_assistant(self, user_question:str) -> str:
        """
        Maps a user's natural language question on cooking.
        :param user_question: str, user's cooking question
        :return: str
        """
        try:
            answer = super().chat_assistant(
                question=user_question,
                )
            
            return answer
        except Exception as e:
            return f"Internal error '{str(e)}'"

