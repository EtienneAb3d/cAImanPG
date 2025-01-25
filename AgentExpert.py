import json
import re
from Agent import Agent

class AgentExpert(Agent):
    """
    The Expert agent is analyzing the request from the first agent to identify a possible known question listed in a FAQ. 
    If a known question is identified, it provides with the known procedure to solve the problem.
    """
    def __init__(self):
        super().__init__(system_prompt = "You are an AI assistant that maps user questions in natural language to the best predefined FAQ questions.")
        self.faq_data = self.load_faq('data_test_python.json')
        self.not_found = "Sorry, I couldn't find an exact match. Please contact support."

    def load_faq(self, file_path:str):
        with open(file_path, 'r') as file:
            return json.load(file)

    def chat_assistant(self, user_question:str) -> str:
        """
        Maps a user's natural language question to a preset FAQ question.
        :param user_question: str, user's technical question
        :return: str, mapped FAQ answer or not_found string
        """
        try:
            # This part could be replaced by a Live database call
            known_questions = []
            known_answers = {}
            for scenario in self.faq_data["troubleshooting_scenarios"]:
                known_questions.append(scenario['issue'])
                known_answers[scenario['issue']] = scenario['steps']

            answer = super().chat_assistant(
                question=f"Which FAQ question does this match: '{user_question}'? Choose the best string from this list and provide it enclosed between <> markers: \n{"\n".join(known_questions)}",
                )
            
            mapped_question = answer.strip()
            if not mapped_question:
                return self.not_found
            mapped_question = re.sub(r'(^.*<|>.*$)',"",mapped_question)
            if mapped_question not in known_questions:
                return self.not_found
            return f"For this problem: {mapped_question}\nFollow these instructions:\n- {"\n- ".join(known_answers[mapped_question])}"
        except Exception as e:
            return self.not_found

