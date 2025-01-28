import os
from Utils import load_hf_token
import asyncio

os.environ["HF_TOKEN"] = load_hf_token("hf_token.txt")
# This configuration is ok to run with 2 RTX 3060 with 12G Video-RAM each
command = "vllm serve mistralai/Mistral-7B-Instruct-v0.3 --port 8001 --dtype float16 --api-key 'cubAIx' --tensor-parallel-size 2 --max_model_len 16384"

async def run_command(command):
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    print(f"Running command: {command}")
    
    # Read stdout and stderr line by line
    while True:
        # Wait for output
        stdout_line = await process.stdout.readline()
        stderr_line = await process.stderr.readline()

        # Check if both streams are exhausted
        if not stdout_line and not stderr_line:
            break

        # Print each line as it comes
        if stdout_line:
            print(f"STDOUT: {stdout_line.decode().strip()}")
        if stderr_line:
            print(f"STDERR: {stderr_line.decode().strip()}")

    # Wait for the command to finish
    return_code = await process.wait()
    print(f"Command exited with return code {return_code}")

# Main coroutine
async def main():
    await run_command(command)

# Run the event loop
asyncio.run(main())
