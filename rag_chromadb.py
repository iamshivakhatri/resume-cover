import os
import requests
from bs4 import BeautifulSoup

# Set USER_AGENT environment variable
os.environ['USER_AGENT'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

# Define the URL and custom headers
url = "https://www.tesla.com/careers/search/job/machine-learning-engineer-motion-planning-self-driving-221945"
headers = {
    "User-Agent": os.environ.get('USER_AGENT', 'Mozilla/5.0')
}

# Fetch the webpage
response = requests.get(url, headers=headers)
response.raise_for_status()  # Ensure we notice bad responses

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and print the content
page_data = soup.get_text()
print("Page data:", page_data[:1000])  # Print the first 1000 characters for brevity
