# using GPT-4 (32k tokens), takes in input from prompt.txt and writes output to result.txt
import openai
import os

# Replace with your actual API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Read the prompt from the file
with open("prompt.txt", "r") as prompt_file:
    prompt = prompt_file.read()

response = openai.ChatCompletion.create(
    model="gpt-4", # 32k is not available yet, should be "gpt-4-32k"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(response)

# Extract the assistant's response
assistant_response = response['choices'][0]['message']['content']

# Write the response to the output file
with open("result.txt", "w") as result_file:
    result_file.write(assistant_response)