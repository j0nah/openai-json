import openai
import json
openai.api_key = "<INSERT YOUR API KEY>"

prompt = "Return 10 recipes that require avocado"

set_recipe_schema = {
  "type": "object",
  "properties": {
    "recipes": {
      "type": "array",
      "items": {"type": "string"},
      "description": "a list of recipes requiring an avocado"
    },
  }
}

response = openai.ChatCompletion.create(
    model="gpt-4",
  messages= [
    { "role": "system", "content": "You are a helpful AI assistant." },
    { "role": "user", "content": prompt }],
    functions= [
        { "name": "set_recipe", "parameters": set_recipe_schema },
      ],
)

function_call = response["choices"][0]["message"]["function_call"]
print("Calling: {} with argument \n{}".format(function_call["name"], json.loads(function_call["arguments"])))