import json
with open("tests.json") as f:
    tests = json.load(f)
    f.close()

with open("values.json") as f:
    values = json.load(f)
    f.close()

d={}
for x in values['values']:
    d[x['id']] = x['value']

def set_value(sp):
    sp['value'] = d[sp['id']]
    if sp.setdefault("values", False):
        for x in sp['values']:
            x = set_value(x)
    return sp

with open('report.json', 'w') as outfile:
    json.dump(set_value(tests), outfile)
