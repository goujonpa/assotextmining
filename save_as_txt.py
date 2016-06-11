# gets all the asso posts and puts it in a single .txt file

import json


with open("cleaned_assoc_0.txt", "r") as in_file:
    data = json.loads(in_file.read())

txt = ''
for i in range(0, len(data)-1):
    txt += data[i]["message"]
    txt += ' '

with open("corpus.txt", "w") as corpus:
    corpus.write(txt.encode('utf8', 'replace'))
