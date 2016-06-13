# gets all the asso posts and puts it in a single .txt file

import json
import os


txt_250 = list()
txt_500 = list()
txt_1000 = list()
txt_1500 = list()
txt_plus = list()
stats_250 = list()
stats_500 = list()
stats_1000 = list()
stats_1500 = list()
stats_plus = list()
varrad = u'txt_'
varrad2 = u'stats_'


for i in range(0, 51):
    try:
        with open(("./data/cleaned_assoc_" + str(i) + ".txt"), "r") as in_file:
            data = json.loads(in_file.read())
    except Exception as e:
        print("Error " + str(i) + str(e))

    for j in range(0, len(data)):
        try:
            msg = data[j]["message"]
            if len(msg.replace('\n', '').replace(' ', '')) <= 250:
                suffix = '250'
            elif len(msg.replace('\n', '').replace(' ', '')) <= 500:
                suffix = '500'
            elif len(msg.replace('\n', '').replace(' ', '')) <= 1000:
                suffix = '1000'
            elif len(msg.replace('\n', '').replace(' ', '')) <= 1500:
                suffix = '1500'
            else:
                suffix = 'plus'

            txt = eval(varrad + suffix)
            txt.append("\n========== Page : " + str(i) + " Post : " + str(j) + "\n")
            txt.append('Characters number (no space no linebreak):' + str(len(msg.replace('\n', '').replace(' ', ''))) + '\n')
            txt.append('Line breaks : ' + str(msg.count('\n')) + '\n')
            txt.append('? number : ' + str(msg.count('?')) + '\n')
            txt.append('! number : ' + str(msg.count('!')) + '\n')
            txt.append('[ number : ' + str(msg.count('[')) + '\n')
            txt.append('FROM : ' + data[j]['from']['name'] + '\n')
            #txt.append('DATE : ' + data[j]['update_time'] + '\n')
            txt.append('MESSAGE : ' + msg + '\n')
            txt.append('============================\n\n============================\n\n')
            stat = eval(varrad2 + suffix)
            stat.append([len(msg.replace('\n', '').replace(' ', '')), msg.count('\n'), msg.count('?'), msg.count('!'), msg.count('[')])

        except Exception as e:
            print("Error file " + str(i) + " msg " + str(j) + " : " + str(e))

sums = {
    '250': [sum(col) for col in zip(*stats_250)],
    '500': [sum(col) for col in zip(*stats_500)],
    '1000': [sum(col) for col in zip(*stats_1000)],
    '1500': [sum(col) for col in zip(*stats_1500)],
    'plus': [sum(col) for col in zip(*stats_plus)],
}

for i in [250, 500, 1000, 1500, 'plus']:
    char_mean = sums[str(i)][0] / float(len(eval('stats_' + str(i))))
    lb_mean = sums[str(i)][1] / float(len(eval('stats_' + str(i))))
    qu_mean = sums[str(i)][2] / float(len(eval('stats_' + str(i))))
    exc_mean = sums[str(i)][3] / float(len(eval('stats_' + str(i))))
    brack_mean = sums[str(i)][4] / float(len(eval('stats_' + str(i))))
    txt = eval('txt_' + str(i))
    txt.append(('\n\nCharacter mean : ' + str(char_mean) + '\nLine breaks mean : ' + str(lb_mean) + '\n? mean : ' + str(qu_mean) + '\n! mean :' + str(exc_mean) + '\n[ mean :' + str(brack_mean) + '\n\n'))

txt_250 = ''.join(txt_250)
txt_500 = ''.join(txt_500)
txt_1000 = ''.join(txt_1000)
txt_1500 = ''.join(txt_1500)
txt_plus = ''.join(txt_plus)

try:
    for i in [250, 500, 1000, 1500, 'plus']:
        with open(("./data_gabriel/" + str(i) + ".txt"), "w") as corpus:
            txt = eval('txt_' + str(i))

            corpus.write(txt.encode('utf8', 'replace'))
except Exception as e:
    print("Error while writing final file : " + str(e))
