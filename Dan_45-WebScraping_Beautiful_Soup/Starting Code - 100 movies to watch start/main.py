import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

titles = soup.find_all("h3", class_="title")

# Create a list of tuples to store movie numbers and titles
movies = []

for title in titles:
    naziv_ceo = title.getText()
    broj = title.getText().split(" ")[0].replace(")","").replace(":","")
    naslov = " ".join(naziv_ceo.split(" ")[1:])
    movies.append((int(broj), naslov))

# Sort the list of tuples by movie numbers
sorted_movies = sorted(movies)

# Print the sorted movies
for number, title in sorted_movies:
    print(f"{number}: {title}")
