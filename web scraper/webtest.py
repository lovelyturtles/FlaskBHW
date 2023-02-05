from bs4 import BeautifulSoup
import requests
import re 
import pandas as pd
import numpy as np

# https://www.healthgrades.com/physician/dr-aida-beckerly-g8k4j

url = "https://www.healthgrades.com/physician/dr-ilan-tur-kaspa-394tt"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

girl_names = pd.read_csv("test_code/girl_names_2000.csv")

ratings = np.array([])
userate = doc.find_all(class_ = "s6RLV")
name_list = ([])
name_tags = doc.find_all(class_ = "c-single-comment__commenter-info")

for i in range(len(name_tags)):
    name = name_tags[i].text.split(" ")[0]
    user_rating = userate[i]["aria-label"].split(" ")[-1]
    if len(name_tags) > 1:
        if name in girl_names.values:
            name_list.append(name)
            ratings = np.append(ratings, int(user_rating))
        elif name[-1] == "a":
            name_list.append(name)
            ratings = np.append(ratings, int(user_rating))
        else:
            name_list = name_list
            ratings = ratings
    else:
        x = x
        # move onto next physician url
# selects name by index on review page
# loops through all first names and compare to list of women's names
# adds reviewer name and rating to array if in list of names

dr_tag = doc.find("h1").text
# extracts dr name from page

spec_tag = doc.find("h2").text
# specialty

rate_tag = doc.find(class_ = "star-reviews-count star-reviews-standard-redesign").text.split(" ")[0]
# extracts the total rating from page

add_tag = doc.find(class_ = "location-row-address").text
# address

ave_femr = sum(ratings)/len(ratings)
# average women rating

dict = {"Doctor Name": dr_tag, "Specialty": spec_tag, "Average Women Rating": ave_femr, "Address": add_tag}

print(dict)

#  next step: 
# (1) parse multiple webpages
# (2) integrate with rest of website

# .find() returns first result
# .find_all() returns all results matching query
