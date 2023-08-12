import openai
import json
openai.api_key = "<INSERT YOUR API KEY>"

prompt = "j0nah has email address: contact@j0nah.com and phone number: 222-456-4564. He is a customer at Acme Computers Limited. He typically prefers emails but will take a text message on the weekend. Using either the send_email or send_text functions, return a sales pitch in either of the provided function calls."

## specify the input and function names of the functions you want OpenAI to know about
send_email_schema = {
  "type": "object",
  "properties": {
    "email_address": {
      "type": "string",
      "description": "The customers email address"
    },
    "body": {
      "type": "string",
      "description": "a short sales pitch to the customer for acme computer"
    }
  }
}

send_text_schema = {
  "type": "object",
  "properties": {
    "phone_number": {
      "type": "string",
      "description": "The customers phone number"
    },
    "body": {
      "type": "string",
      "description": "a short sales pitch to the customer for acme computer"
    },
  }
}

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages = [
    { "role": "system", "content": "You are a helpful AI assistant." },
    { "role": "user", "content": prompt }],
  functions = [
    { "name": "send_email", "parameters": send_email_schema },
    { "name": "send_text", "parameters": send_text_schema }
  ]
)

function_call = response["choices"][0]["message"]["function_call"]
print("Calling: {} with argument \n{}".format(function_call["name"], json.loads(function_call["arguments"])))