import json
import requests
def gender():
    name = raw_input("Enter name to determine the gender ")
    gender_json = "http://api.genderize.io/?name=" + name
    gresp = requests.get(gender_json)
    gresp = json.loads(gresp.content)

    print gresp["gender"]
    
gender()
