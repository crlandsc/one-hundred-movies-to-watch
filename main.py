import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
webpage_html = response.text
soup = BeautifulSoup(webpage_html, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
movie_titles_text = []
for movie_title in movie_titles:
    text = movie_title.getText() #.split(")")  # Can't split because there is a typo in Godfather II from the site
    movie_titles_text.append(text)

# print(movie_titles_text)
# top_100_movies = [movie for movie in reversed(movie_titles_text)]  # Reverses list
top_100_movies = movie_titles_text[::-1]  # reverses list
print(top_100_movies)

with open("movies.txt", "w") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")
