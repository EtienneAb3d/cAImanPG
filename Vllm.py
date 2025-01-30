import os
from Config import load_hf_token,get_model
import subprocess
import time

try:
    os.environ["HF_TOKEN"] = load_hf_token("hf_token.txt")
except Exception as e:
    print(f"Can't load hf_token.txt: {str(e)}")


model_familly,model,url,api_key = get_model()
commands = [
    # May need to remove locks from a previously interrupted download: 
    # rm -rf ~/.cache/huggingface/hub/.locks/*
    # May need to add '--force-download' option after a bad download
    f"huggingface-cli download {model}",
    # This 'vllm serve' configuration is ok to run with 2 RTX 3060 with 12G Video-RAM each
    f"vllm serve {model} --port 8001 --dtype float16 --api-key 'cubAIx' --tensor-parallel-size 2 --max_model_len 8192",
    ]

def run_command(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        universal_newlines=True,
        shell=True,
    )

    print(f"Running command: {command}")
    
    # Read stdout and stderr line by line
    while True:
        stdout_line = process.stdout.readline()
        stderr_line = process.stderr.readline()

        if stdout_line:
            print(f"STDOUT: {stdout_line}")
        if stderr_line:
            print(f"STDERR: {stderr_line}")

        # Check if the process has finished
        if process.poll() is not None:
            break

        # Avoid excessive CPU usage
        time.sleep(0.1)

for command in commands:
    run_command(command)
