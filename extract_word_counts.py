import json
from bs4 import BeautifulSoup

with open("data/words.html") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

word_counts = dict()

for line in soup.find_all("a", "line"):
    word = line.find("div", class_="word").text
    count = line.find("div", class_="count").text
    count = int(count.replace(',', ''))
    word_counts[word] = count

with open("data/word_counts.json", 'w') as f:
    json.dump(word_counts, f)
