import requests

def save_html_to_file(url, output_file):
    try:
        # Send an HTTP request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Save the HTML content to a text file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"HTML content saved to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage:
url_to_scrape = 'https://techcrunch.com/2023/10/27/x-is-launching-new-premium-and-basic-subscription-tiers/'
KingLaiTextFile = 'KingLaiText.txt'

save_html_to_file(url_to_scrape, KingLaiTextFile)
