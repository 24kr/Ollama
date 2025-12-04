import ollama

# # The ollama.list() function queries the Ollama API to get a list of all models
# # that are available locally on your machine.
# # This is useful for programmatically checking which models you can use.
# response = ollama.list()
# print(response)

# # This is a standard, non-streaming call to the chat API.
# # The program sends the entire request and waits for the full response
# # from the model before proceeding to the next line of code.
# res = ollama.chat(
#     model="llama3.2", # Specifies which model to use for the chat.
#     # The 'messages' parameter takes a list of message objects.
#     # This structure allows for maintaining a conversation history with the model.
#     messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]
#     )
# # The response object 'res' is a dictionary. The actual text from the model
# # is located under the path ["message"]["content"].
# print(res["message"]["content"])

# # This is a streaming call to the chat API, enabled by `stream=True`.
# # Instead of waiting for the full response, it returns a generator immediately.
# res = ollama.chat(
#     model="llama3.2",
#     messages=[{'role': 'user', 'content': 'Tell me a joke about computers.'}],
#     stream=True,
# )

# # We iterate over the generator to receive the response in chunks as it's created.
# # This provides a real-time, "typing" effect for a better user experience.
# for chunk in res:
#     # 'end=""' prevents adding a newline after each chunk, printing them sequentially.
#     # 'flush=True' ensures the output is printed to the console immediately.
#     print(chunk["message"]["content"], end="", flush=True)

# # The ollama.show() function retrieves and prints detailed information
# # about a specific model, including its parameters, template, and other metadata.
# print(ollama.show("llama3.2"))


ollama.create(
    model="knowitall",
    from_='llama3.2',
    system="You are a very smart assistant who knows everything about the ocean. You are very succinct and informative."
)

# Parameters like 'temperature' are now passed in an 'options' dictionary
# during the generation step.
res = ollama.generate(
    model="knowitall",
    prompt="Why is the ocean so salty?",
    options={
        'temperature': 0.1
    }
)

if "response" in res:
    print(res["response"])

# delete model
ollama.delete("knowitall")