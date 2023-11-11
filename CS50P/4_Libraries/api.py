# API's third party services that we can write code to interact with
# JSON JavaScript Object Notation - a language agnostic format for exchanging data between computers
#import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=25&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))  # prints the entire return value, too much info

o = response.json()
for result in o["results"]:
    print(result["trackName"], " Album:", result["collectionName"], "Track#:", result["trackNumber"], "Disc#", result["discNumber"])
    
    



    
    