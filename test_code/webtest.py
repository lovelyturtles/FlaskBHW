from bs4 import BeautifulSoup
import requests
import re 

# https://www.healthgrades.com/physician/dr-aida-beckerly-g8k4j


url = "https://www.healthgrades.com/physician/dr-aida-beckerly-g8k4j"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

tags = doc.find_all(class_ = "c-single-comment__commenter-info")

#for tag in tags:
    print tag.

print(type(tags))




# tag = doc.find_all(["span"], string contains "Pamela P. in Chicago, IL – ")


# .find() returns first result
# .find_all() returns all results matching query