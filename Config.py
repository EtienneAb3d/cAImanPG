# May be local intranet "Mistral, "Llama", "DeepSeek", "Lucie" or internet "ChatGPT"
llm = "Mistral"
def get_model():
        if llm == "Mistral":
            return llm,"meta-llama/Meta-Llama-3-8B-Instruct",'http://localhost:8001/v1', 'cubAIx'
        elif llm == "Llama":
            return llm,"mistralai/Mistral-7B-Instruct-v0.3",'http://localhost:8001/v1', 'cubAIx'
        elif llm == "DeepSeek":
            return llm,"deepseek-ai/DeepSeek-R1-Distill-Llama-8B",'http://localhost:8001/v1', 'cubAIx'
        elif llm == "Lucie":
            return llm,"OpenLLM-France/Lucie-7B-Instruct",'http://localhost:8001/v1', 'cubAIx'
        else:
            return llm,"gpt-4",None, load_api_key('openai_api_key.txt')

def load_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def load_hf_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
