#!/usr/bin/py -3

import json

conf = {}
conf['newkey'] = 5.00005

with open('backup_config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',',': '))

with open("backup_config.json", 'r') as fh:
    conf = json.load(fh)

print(conf)
