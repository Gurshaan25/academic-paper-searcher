import subprocess

def ollama_generate(prompt: str, model: str = "llama3"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()
