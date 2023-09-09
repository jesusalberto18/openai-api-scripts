import openai
openai.api_key = "sk-..."  # supply your API key however you choose

# choose text to embed
text_string = "sample text"

# choose an embedding
model_id = "text-embedding-ada-002"

# compute the embedding of the text
embedding = openai.Embedding.create(input=text_string, model=model_id)['data'][0]['embedding']
