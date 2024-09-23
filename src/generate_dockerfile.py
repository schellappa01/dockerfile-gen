import os
from openai import AzureOpenAI
import re

def generate_dockerfile_with_ai(java_version, packaging, framework, port):
    # Replace with your actual Azure OpenAI API key
    api_key = os.getenv('AZURE_OPENAI_API_KEY', '7b00d06efa7a4e1f90264357886bcb58')
    # Replace with your Azure OpenAI endpoint
    azure_endpoint = "https://docker-generation.openai.azure.com/"

    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_key=api_key,
        api_version="2024-02-01",
        azure_endpoint=azure_endpoint
    )

    # Deployment name (this should be your model deployment name)
    deployment_name = "docker-generation"

    # Formulate the prompt

    prompt = (
    f"Generate a Dockerfile for a Java project using version {java_version}, "
    f"packaging as {packaging}, utilizing the {framework} framework, and running on port {port}. "
    f"Provide only the Dockerfile content. Do not include any additional text, questions, explanations, or examples."
)


    print('prompt = ', prompt )
    # Send the completion call
    response = client.completions.create(
        model=deployment_name,
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Return the Dockerfile content
    dockerfile_content = response.choices[0].text.strip()
   
    # Extract the Dockerfile content
    # Use regex to find the Dockerfile block
    match = re.search(r'```dockerfile\n(.*?)\n```', dockerfile_content, re.DOTALL)
    if match:
        dockerfile_content = match.group(1).strip()
        print(dockerfile_content)
    else:
        print("Dockerfile content not found.")

    return dockerfile_content
