import urllib.request
import json

source = urllib.request.urlopen('https://data.cityofnewyork.us/resource/jb7j-dtam.json?$limit=2000')

raw_data = source.read()
decoded_data = raw_data.decode('utf-8')
data = json.loads(decoded_data)
w = open("./data/Shaws_clean_data.csv", "w")

headings = list(data[0].keys())
heading = []
for h in headings:
    s = ""
    for char in h:
        if char == "_":
            s += " "
        else:
            s += char
    headings[headings.index(h)] = s.title()
w.write(",".join(headings))
#I changed this line from "".join(headings) to ",".join(headings)
w.write("\n")

for i in data:
    w.write(",".join(i.values()))
    w.write("\n")

w.close()


