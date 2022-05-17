import requests
from bs4 import BeautifulSoup
with open("updated_raw_text_script_urls.txt") as file:
    text = file.readlines()
names = []
urls = []
for i in text:
    split_text = i.split(" +++$+++ ")
    names.append(split_text[1].strip())
    urls.append(split_text[2].strip())
def scrape(url):
    response = requests.get(url)
    return response.text
for i in range(len(text)):
    scr = scrape(urls[i])
    soup = BeautifulSoup(scr, "html.parser")
    filename = names[i] + ".txt"
    with open(filename, 'w') as f:
        f.write(soup.text)

