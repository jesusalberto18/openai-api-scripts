import openai
openai.api_key = "sk-..."  # supply your API key however you choose

completion = openai.Completion.create(model="davinci-002", prompt="Hello world")
print(completion.choices[0].text)
