import requests
from bs4 import BeautifulSoup

# Open the file containing the accession numbers to search for
with open("accession_numbers.txt", "r") as f:
    accession_numbers = [line.strip() for line in f.readlines()]

# Define the URL format for the NCBI search page
url_format = "https://www.ncbi.nlm.nih.gov/sra?term={}"

# Initialize a dictionary to store the unique identifiers
unique_ids = {}

# Loop over the accession numbers and search for each one on NCBI
for accession_number in accession_numbers:
    # Construct the URL for the NCBI search page
    url = url_format.format(accession_number)

    # Make a GET request to the URL and parse the response using BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the unique identifier on the page (which should start with "PRJ")
    unique_id = None
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href and href.startswith("/bioproject/PRJ"):
            unique_id = href.split("/")[-1]
            break

    # Add the unique identifier to the dictionary
    unique_ids[accession_number] = unique_id

# Save the unique identifiers to a text file
with open("unique_ids.txt", "w") as f:
    for accession_number, unique_id in unique_ids.items():
        f.write(f"{accession_number}\t{unique_id}\n")
