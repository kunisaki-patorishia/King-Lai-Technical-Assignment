import openai
import json

# Your OpenAI API key
openai.api_key = 'my_API_Code'

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

# Save the result in JSON format
output_json_path = 'output_result with OpenAI.json'  # Replace with your desired output path
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, indent=2)

print(f"Result saved to {output_json_path}")
