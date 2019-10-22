# JSON files
import json

# json.dump expample
movie = {}  # create a dictionary
movie["title"] = "Minority Report"
movie["director"] = "Steven Spielberg"
movie["composer"] = "John Williams"
movie["actors"] = ["Tom Cruise", "Colin Farrel", "Samantha Morton", "Max von Sydow"]
movie["is_awesome"] = True
movie["budget"] = 102000000
movie["cinematographer"] = "Janusz Kami\u0144ski"

file = open("movie.json", "w", encoding = "utf-8")
json.dump(movie, file, ensure_ascii = False)
file.close()

# json.load example
file = open("movie.json", "r", encoding = "utf-8")
movie = json.load(file)
file.close()

[print(actor) for actor in movie["actors"] if actor.split(' ')[-1].startswith('S')]
