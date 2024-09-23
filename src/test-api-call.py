import os
from openai import AzureOpenAI

# Set the API key directly as a string (you should replace 'YOUR_API_KEY' with your actual key)
client = AzureOpenAI(
    api_key="7b00d06efa7a4e1f90264357886bcb58",  # Replace with your actual Azure OpenAI API key
    api_version="2024-02-01",
    azure_endpoint="https://docker-generation.openai.azure.com/"
)

# This should correspond to the custom name you chose for your deployment.
deployment_name = "docker-generation"

# Send a completion call to generate an answer
prompt = "Generate a Dockerfile for a Java project"
response = client.completions.create(
    model=deployment_name,
    prompt=prompt,
    temperature=1,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

# Print the response
print(prompt + response.choices[0].text)
