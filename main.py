import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
response = requests.get("https://books.toscrape.com/")

# Parse the HTML content of the website
soup = BeautifulSoup(response.text, "html.parser")

# Extract the data you want using Beautiful Soup's various methods and attributes
titles = soup.find_all("h3")
prices = soup.find_all(class_="price_color")

# Save the extracted data to a file or database, or use it for some other purpose
with open("book_data.txt", "w") as file:
    for title, price in zip(titles, prices):
        file.write(f"{title.text}: {price.text}\n")