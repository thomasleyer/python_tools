#!/usr/bin/python

import yaml
import glob
tools= []

output_format = ["name", "category", "type", "purpose", "license", "license_url", "license_checked_date", \
                 "license_checked_by", "security_patches_checked_date", "secuirty_patches_checked_by", \
                 "remarks", "install_base"]



configs = map(lambda x: yaml.load_all(open(x)), glob.glob("*.yaml"))
for config in configs:
  for item in config:
    if item["name"]=="categories":
      categories=item["categories"]
    else:
      tools.append(item)

#### output for xls2md

output_header1 = "|"
output_header2 = "|"

for i in output_format:
  output_header1 += i + "|"
  output_header2 += "-----|"

print output_header1
print output_header2

for tool in tools:
  if tool["category"] not in categories:
    print "FAIL: no valid category"
  output = "|"
  for i in output_format:
    output += tool.get(i, "-") + "|"
  print output
