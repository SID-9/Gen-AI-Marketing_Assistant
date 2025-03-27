import ollama

try:
    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": "Hello, how are you?"}])
    print(response)
except Exception as e:
    print(f"Error: {e}")
