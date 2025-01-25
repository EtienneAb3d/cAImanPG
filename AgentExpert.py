import openai
import json
import re
from Utils import load_api_key

class AgentExpert:
    def __init__(self):
        self.api_key = load_api_key('openai_api_key.txt')
        self.faq_data = self.load_faq('data_test_python.json')
        openai.api_key = self.api_key

    def load_faq(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def map_question_to_faq(self, user_question):
        """
        Maps a user's natural language question to a preset FAQ question.
        :param user_question: str, user's technical question
        :return: str, mapped FAQ question or None
        """
        try:
            known_questions = []
            known_answers = {}
            for scenario in self.faq_data["troubleshooting_scenarios"]:
                known_questions.append(scenario['issue'])
                known_answers[scenario['issue']] = scenario['steps']
            messages=[
                    {"role": "system", "content": "You are an AI assistant that maps user questions in natural language to the best predefined FAQ questions."},
                    {"role": "user", "content": f"Which FAQ question does this match: '{user_question}'? Choose the best string from this list and provide it enclosed between <> markers: \n{"\n".join(known_questions)}"}
                ]
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=100,
                temperature=0.3
            )
            
            mapped_question = response.choices[0].message.content.strip()
            if not mapped_question:
                return None
            mapped_question = re.sub(r'(^.*<|>.*$)',"",mapped_question)
            if mapped_question not in known_questions:
                return None
            return f"For this problem: {mapped_question}\nFollow these instructions:\n- {"\n- ".join(known_answers[mapped_question])}"
        except Exception as e:
            return None

    def get_technical_answer(self, user_question):
        """
        Gets technical support answers using a local FAQ or AI.
        :param user_question: str, user's technical question
        :return: str, answer to the question
        """
        mapped_question = self.map_question_to_faq(user_question)
        if mapped_question:
            return mapped_question
        
        return "Sorry, I couldn't find an exact match. Please contact support."

