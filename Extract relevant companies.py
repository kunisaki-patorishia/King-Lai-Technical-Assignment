import openai
import json

# Your OpenAI API key
openai.api_key = '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'

def extract_information(text):
    prompt = "Extract relevant information from the given text:\n"
    example = f"{prompt}{text}"

    response = openai.Completion.create(
        engine="text-davinci-002-ft",  # Replace with the correct and supported model
        prompt=example,
        temperature=0.7,
        max_tokens=150
    )

    extracted_info = response.choices[0].text.strip()

    return json.loads(extracted_info)

# Load HTML content from the saved text file
with open('KingLaiText.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Extract information using the function
result = extract_information(html_content)

# Print or save the result
print(json.dumps(result, indent=2))
