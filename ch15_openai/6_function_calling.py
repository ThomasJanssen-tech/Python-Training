from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

tools = [{
    "type": "function",
    "name": "get_population_data",
    "description": "Get the population of a country",
    "parameters": {
        "type": "object",
        "properties": {
            "country": {
                "type": "string",
                "description": "The 2 digit country code (ISO 3166-1 alpha-2)",
            }
        },
        "required": [
            "country"
        ],
        "additionalProperties": False
    }
}]

def get_population_data(country):
    if(country == "NL"):
        return {"population": 17134872, "country": "Netherlands"}
    elif(country == "BE"):
        return {"population": 11589623, "country": "Belgium"}


input_messages = [{"role": "user", "content": "How many people live in the Netherlands?"}]


response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools
)


tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = get_population_data(args["country"])

input_messages.append(tool_call)  # append model's function call message
input_messages.append({                               # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)
print(response_2.output_text)