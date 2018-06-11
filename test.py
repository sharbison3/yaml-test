import io
import pprint
import sys
import yaml

with open("test.yaml") as f:
    data = yaml.safe_load(f)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)

keys = set(k for k, v in data["overrides"].iteritems())
print keys

