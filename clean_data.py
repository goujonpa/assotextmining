# Helper to clean our data

begin_page = 0

import os
import json

# load data
with open("fb_output.json", "r") as data_file:
    data = data_file.read()
    data = json.loads(data)

# For data in the dataset display it to the user in a formatted way so that the
# user can choose whether that's associative communication or not
for i in range(begin_page, len(data)):
    associative_cleaned = list()
    other_cleaned = list()
    # For each pages
    for j in range(0, len(data[str(i)])):
        # For each messages in each pages

        # clean console
        os.system('clear')
        print("Msg " + str(j + 1) + "/" + str(len(data[str(i)])) + " - Page " + str(i) + "/" + str(len(data)))
        try:
            print("\nFrom: " + data[str(i)][j]['from']['name'])
            print("\nMessage:\n" + data[str(i)][j]['message'])
        except Exception, e:
            print("Exception: " + str(e))
        user_input = raw_input("\n\n\n\nAssociatif ?")
        if user_input == 'y':
            # if associative 
            associative_cleaned.append(data[str(i)][j])
        elif user_input == 'q':
            # if quit 
            break
        else:
            # if other
            other_cleaned.append(data[str(i)][j])

    # at each page end (about 100 message by page), dump
    filename = "cleaned_assoc_" + str(i) + ".txt"
    with open(filename, "w") as out_file:
        out_file.write(json.dumps(associative_cleaned, sort_keys=True, indent=4,
            separators=(',', ':')))

    filename = "cleaned_other_" + str(i) + ".txt"
    with open(filename, "w") as out_file:
        out_file.write(json.dumps(other_cleaned, sort_keys=True, indent=4,
            separators=(',', ':')))

    if user_input == 'q':
        exit(1)
