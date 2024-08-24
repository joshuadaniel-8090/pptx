import os
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = input("Enter the URL: ")
#url = "https://tamilchristiansongs.in/lyrics/aathmame-un-aandavarin"  # Replace with the actual URL

# Directory to save the output Markdown file
output_directory = "md"

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Path for the Markdown file
file_name = input("Name of the file: ")
markdown_file = os.path.join(output_directory, file_name)

# Function to scrape content and save it directly as a Markdown file
def scrape_and_save_as_markdown(url, output_file):
    """
    Scrape content from the webpage by the specific ID 'tamiltext' and save it as a markdown file.

    Args:
    - url: The URL of the webpage to scrape.
    - output_file: The path to the output markdown file.
    """
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract content by the specific ID 'tamiltext'
        specific_content = soup.find(id='tamiltext')
        with open(output_file, "w", encoding="utf-8") as file:
            if specific_content:
                specific_text = specific_content.get_text()
                # Writing directly to the markdown file
                file.write("# Content with ID 'tamiltext'\n\n")
                file.write(specific_text + "\n\n")
            else:
                file.write("# No content found with ID 'tamiltext'\n\n")

        print(f"Content has been successfully extracted and saved to '{output_file}'.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Scrape the content from the webpage and save it directly to a markdown file
    scrape_and_save_as_markdown(url, markdown_file)
