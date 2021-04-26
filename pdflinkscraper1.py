import fitz
import re

url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

file = "test.pdf"

with fitz.open(file) as pdf:
    text = ""
    
    for page in pdf:

        text += page.getText()

urls = []

#extract urls using the regular expression

for match in re.finditer(url_regex, text):

    url = match.group()

    print("[+] URL Found:", url)

    urls.append(url)

print ("[*] Total URLS Found:", len(urls))
