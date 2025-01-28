def load_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def load_hf_token(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
