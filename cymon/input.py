from cymon import Cymon
import json
import csv
api = Cymon('8d839c293762a7fe740d39decd0c86688f56489e')
#inp = input()
#yo = api.ip_lookup(inp)
#with open('data.json', 'w') as outfile:
 #   json.dump(yo, outfile)
blacklist = [
    'malware',
    'botnet',
    'c2',
    'zombie',
    'phishing',
    'ransomware',
    'malvertising',
    'ek',
    'scan',
    'bruteforce',
    'proxy',
    'tor',
    'vpn',
    'malicious activity',
    'blacklist',
    'dnsbl'
]
for i in blacklist:
	tag = api.ip_blacklist(i)
	with open(i+'.json', 'w') as outfile:
	    json.dump(tag, outfile)
	inputfile = open(i+'.json','r')
	outfile = open(i+'.csv','w')
	writer = csv.writer(outfile)
	for row in json.loads(inputfile.read()):
		writer.writerow(row)
		print(row)








"""print("enter tag")
tag_inp = input()
tag = api.ip_blacklist(tag_inp)
with open(tag_inp+'.txt', 'w') as outfile:
    json.dump(tag, outfile)

print(tag)

#parsed = json.loads(yo)
#print json.dumps(parsed, indent=4, sort_keys=True)"""

