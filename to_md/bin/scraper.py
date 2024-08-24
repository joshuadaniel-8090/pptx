import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://tamilchristiansongs.in/lyrics/aathmame-un-aandavarin"  # Replace with the actual URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Open a file to save the extracted text
    with open("extracted_content.txt", "w", encoding="utf-8") as file:
        # Extract content by the specific ID 'tamiltext'
        specific_content = soup.find(id='tamiltext')
        if specific_content:
            specific_text = specific_content.get_text()
            file.write("Content with ID 'tamiltext':\n")
            file.write(specific_text + "\n\n")  # Write to file
        else:
            file.write("No content found with ID 'tamiltext'.\n")
    
    print("Content has been successfully extracted and saved to 'extracted_content.txt'.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

