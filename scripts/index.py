import os
import requests
from bs4 import BeautifulSoup

# Directory to save the output Markdown files
output_directory = "md/keerthanai"

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to scrape content and save it directly as a Markdown file
def scrape_and_save_as_markdown(url, output_file):
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
                file.write(specific_text + "\n\n")
            else:
                file.write("# No content found with ID 'tamiltext'\n\n")

        print(f"Content has been successfully extracted and saved to '{output_file}'.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Path to the text file containing URLs
    urls_file = 'keerthanai_list_210.txt'  # Replace with the actual path to your file

    # Read each URL from the text file and process it
    with open(urls_file, 'r', encoding='utf-8') as file:
        for i, url in enumerate(file.readlines(), start=1):
            url = url.strip()  # Clean up the URL string
            if url:  # Ensure the URL is not empty
                # Path for the Markdown file, using the index to create unique filenames
                markdown_file = os.path.join(output_directory, f"{i}.md")

                # Scrape the content from the webpage and save it directly to a markdown file
                scrape_and_save_as_markdown(url, markdown_file)
