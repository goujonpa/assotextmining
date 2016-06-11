import datetime
import json
import urlparse
import requests


end_date = datetime.date(2016, 2, 1)
# note : convert back datetime.date.fromtimestamp(test)
response = requests.get('https://graph.facebook.com/170477866300245/feed?access_token=EAACEdEose0cBAK7vjgqoR7SgQcao4lFD2wmmVRclvGRJLUPpoZAXSaMuNchVeTz7LGXazTCxKMFnZBVtsrUIgqtXgpU35lzZBU8snS3YoG0x1gn91K2MxEozJKHaqTdSxBKcoPOP8OxXkfJGZAt7iaOKA68MnYZBXuvZCFquZBEOwZDZD&fields=from,message,id,likes,updated_time&limit=100')
data = json.loads(response.content) 
paging = data['paging']
data = data['data']
i = 0
store = dict()
until = datetime.date(2016, 6, 8)

# while until > 1st feb, 2016
while (until > end_date):
    print(str(i) + ' : ' + str(until) + ' > ' + str(end_date))

    # parse the next url to get the until
    try:
        parsed = urlparse.urlparse(paging['next']) 
        until = urlparse.parse_qs(parsed.query)['until'][0]
        until = datetime.date.fromtimestamp(int(until))
    except Exception as e:
        with open("errored_fb_output.json", "w") as out_file:
            out = json.dumps(store)
            out_file.write(out)
        print("Exception while parsing next url: " + str(e))
     
    # store data
    store[str(i)] = data

    # request next url
    try:
        response = requests.get(paging['next'])
        data = json.loads(response.content) 
        paging = data['paging']
        data = data['data']
    except Exception as e:
        with open("errored_fb_output.json", "w") as out_file:
            out = json.dumps(store)
            out_file.write(out)
        print("Exception while requesting next url: " + str(e))
    i += 1

print('Printing final file')
with open("fb_output.json", "w") as out_file:
    out = json.dumps(store)
    out_file.write(out)

