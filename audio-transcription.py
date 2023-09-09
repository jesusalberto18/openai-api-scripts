# Audio trancription with Whisper
import openai
openai.api_key = "sk-..."  # supply your API key however you choose
f = open("path/to/file.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", f)
