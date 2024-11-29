import requests
import json

# very simple python script that will get the list of options from a rest server 

url = "http://192.168.0.12:3000/teams"

headers = {"User-Agent": "local-jenkins"}

response = requests.request("GET", url, headers=headers).json()
teams_name = response['teams']
print(json.dumps(teams_name, indent=4))

#teams = json.loads(response)
#print(teams['teams'], indent=4)

'''
choices = ""

for team in teams["teams"]:
    choices += team+'\n'

print(choices)
'''