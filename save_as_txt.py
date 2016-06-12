# gets all the asso posts and puts it in a single .txt file

import json


txt = ''
for i in range(0, 51):
    try:
        with open(("cleaned_assoc_" + str(i) + ".txt"), "r") as in_file:
            data = json.loads(in_file.read())
    except Exception as e:
        print("Error " + str(i) + str(e))

    for j in range(0, len(data)):
        try:
            txt += data[j]["message"]
            txt += ' '
        except Exception as e:
            print("Error file " + str(i) + " msg " + str(j) + " : " + str(e))
try:
    with open("./Corpus/final_corpus.txt", "w") as corpus:
        corpus.write(txt.encode('utf8', 'replace'))
except Exception as e:
    print("Error while writing final file")

