import re
import json
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_information(html_content):
    # Example: Extracting the main topic using a simple regex
    main_topic_match = re.search(r'<title>(.*?)</title>', html_content)
    main_topic = main_topic_match.group(1) if main_topic_match else None

    # Process the text with spaCy
    doc = nlp(html_content)

    # Extract company names with improved filtering
    company_names = [ent.text for ent in doc.ents if ent.label_ == "ORG"]

    # Remove duplicates
    unique_company_names = list(set(company_names))

    # Build the result in the desired JSON format
    result = {
        "related_companies": [{"company_name": company, "company_domain": company.lower() + ".com"} for company in unique_company_names],
        "topic": main_topic
    }

    return result

# Load HTML content from the saved text file
file_path = 'KingLaiText.txt'  # Replace with the actual path to your text file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Extract information using the function
result = extract_information(html_content)

# Save the result in JSON format
output_json_path = 'output_result_with_spacy.json'  # Replace with your desired output path
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, indent=2)

print(f"Result saved to {output_json_path}")
