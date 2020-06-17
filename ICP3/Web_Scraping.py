import requests
from bs4 import BeautifulSoup

# url for a wiki page
url = 'https://en.wikipedia.org/wiki/Deep_learning'

# get the information from a url
wiki = requests.get(url)

# parse with beautifulsoup from bs4 library the wiki
soup = BeautifulSoup(wiki.text, "html.parser")
print("Title:", soup.title)

# Find all the links in the page (‘a’ tag)
a_tag = soup.findAll('a')

# Iterate over each tag(above) then return the link using attribute "href" using get
for a in a_tag:
    print(a.get('href'))


# d. Save all the links in the file
with open("result.out", "w") as outfile:
    for link in a_tag:
        outfile.write(f"{link.get('href')}\n")