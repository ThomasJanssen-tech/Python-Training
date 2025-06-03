from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

class Joke(BaseModel):
    joke: str
    explanation: str
    participants: list[str]

client = OpenAI()

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Create a joke with an explanation and participants."},
        {"role": "user", "content": "About werewolves"},
    ],
    response_format=Joke,
)

print(completion.choices[0].message.parsed.joke) 
print(completion.choices[0].message.parsed.explanation)
print(completion.choices[0].message.parsed.participants)
