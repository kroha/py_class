#!/usr/bin/env python

import json
import yaml


a = range(10)
a.append({})
a[-1]['element_1'] = 'some_data'
a[-1]['element_2'] = range(3)

with open("yaml_list.yml","w") as f:
    f.write(yaml.dump(a,default_flow_style=False))

with open("json_list.json","w") as f:                 
    f.write(json.dumps(a))   

print a

