# Async support is available in the API by prepending a to a network-bound method
import openai
openai.api_key = "sk-..."  # supply your API key however you choose

async def create_chat_completion():
    chat_completion_resp = await openai.ChatCompletion.acreate(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# Manually close the client session at the end of your program/event loop
import openai
from aiohttp import ClientSession

openai.aiosession.set(ClientSession())
# At the end of your program, close the http session
await openai.aiosession.get().close()
