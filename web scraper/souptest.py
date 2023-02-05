from bs4 import BeautifulSoup

with open("templates/index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))
 
