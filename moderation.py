import openai
openai.api_key = "sk-..."  # supply your API key however you choose

moderation_resp = openai.Moderation.create(input="Here is some perfectly innocuous text that follows all OpenAI content policies.")
