#!/usr/bin/env python  
import pprint
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto = cisco_cfg.find_objects("crypto map CRYPTO")

group2 = []
aes = []

for i in crypto:
    for b in i.children:
        if b.re_search("group2"):
            group2.append(i.geneology_text)
        if b.re_search("transform-set"):
            if not b.re_search("AES"):
                c = str(i.geneology_text) + " : " + str(b.text)
                aes.append(c)

print "Group 2 crypto maps"
for a in group2:
    print a

print "Non AES"
for a in aes:
    print a
    
