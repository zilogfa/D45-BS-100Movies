# Dev: ali Jafarbeglou - Top 100 Best Movies

from bs4 import BeautifulSoup
import requests
import random

# <....................  WEB SCRAPING -------------------------->
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
bestMoivies = response.text
soup = BeautifulSoup(bestMoivies, "html.parser")

# creating list of movies in reverse
titles = soup.find_all(name="h3", class_="title")
movieTitle = [name.getText() for name in titles][::-1]

# <--------------  CREATING DATA BASE of 100 Top movies as text file from movie list ......................>
with open("movies.txt", "w") as file:
    for name in movieTitle:
        file.write(f"{name}\n")

# <------------------- Generating Random Movies Name from Data Base --------- >
with open("movies.txt", "r") as file:
    name = file.readlines()
    x = random.randint(0, 99)
    print(name[0])