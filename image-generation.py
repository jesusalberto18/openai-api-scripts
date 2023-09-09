# Image generation with Dall-E
import openai
openai.api_key = "sk-..."  # supply your API key however you choose

image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")
