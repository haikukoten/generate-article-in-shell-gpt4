import json
import requests
from language_tool_python import LanguageTool

# GPT-4 API credentials
API_KEY = "your-api-key"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# LanguageTool API setup
lt = LanguageTool("en-US")

# GPT-4 helper function
def generate_chat_completion(messages, model="gpt-4", temperature=0.8, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise Exception(f"Failed to generate completion: {response.text}")

    response_data = response.json()
    return response_data["choices"][0]["message"]["content"]

# Prompt for user input
topic = input("Enter your topic: ")
words = input("Enter number of words: ")

# Format the input for the ChatGPT API
messages = [
    {"role": "system", "content": "You are an AI assistant trained to generate blog posts."},
    {"role": "user", "content": f"Write a detailed and informative blog about {topic} in the context of a comprehensive article and include a title and conclusion(don't create a sub-heading for it), complete the blog within {words} words."},
]

# Send the prompt to the GPT-3.5-turbo Chat Completion API and save the response
generated_message = generate_chat_completion(messages, temperature=0.8, max_tokens=3000)

# Check and correct grammar in the generated text
matches = lt.check(generated_message)
corrected_message = lt.correct(generated_message)
lt.close()

# Display the corrected blog post
print("Generated Blog Post:")
print(corrected_message)
