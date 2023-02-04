from bs4 import BeautifulSoup
import requests
import re 

# https://www.healthgrades.com/physician/dr-aida-beckerly-g8k4j

url = "https://www.healthgrades.com/physician/dr-aida-beckerly-g8k4j"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

name_tags = doc.find_all(class_ = "c-single-comment__commenter-info")
name = name_tags[1].text.split(" ")[0]
# selects name by index on review page
# need to loop through all first names and compare to list of women's names 

number_tags = doc.find_all(type="button", class_ = "summary-standard-phone-link")
#btn_text = number_tags.text
# stuck on this one; might need to use selenium??
# need to toggle button to get information

dr_tag = doc.find("h1").text
# extracts dr name from page

rate_tag = doc.find(class_ = "star-reviews-count star-reviews-standard-redesign").text[0:3]
# extracts the rating from page

# want to:
# extract reviewer name, compare to list of women's names
# if it's a women's name, 


# next step: 
# (1) figure out how parse multiple webpages


# .find() returns first result
# .find_all() returns all results matching query
