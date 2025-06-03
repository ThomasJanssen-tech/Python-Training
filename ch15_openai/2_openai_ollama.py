from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
)

response = client.chat.completions.create(
  model="llama3.2",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a bedtime story about a unicorn"},
  ]
)

print(response.choices[0].message.content)