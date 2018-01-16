from cymon import Cymon
import json
api = Cymon('8d839c293762a7fe740d39decd0c86688f56489e')
inp = input()
yo = api.ip_lookup(inp)
#with open('data.json', 'w') as outfile:
 #   json.dump(yo, outfile)
print("enter tag")
tag_inp = input()
tag = api.ip_blacklist(tag_inp)
with open('blacklist.txt', 'w') as outfile:
    json.dump(tag, outfile)

print(tag)

#parsed = json.loads(yo)
#print json.dumps(parsed, indent=4, sort_keys=True)

