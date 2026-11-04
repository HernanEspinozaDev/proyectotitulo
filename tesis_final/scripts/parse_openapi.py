import re

lines = open('/home/nandev/Documentos/projects/espaciGo/planning/openapi.yaml').readlines()
cur_p = None
cur_m = None
ops = []
for l in lines:
    m = re.match(r'^  (\/[^:]+):', l)
    if m:
        cur_p = m.group(1)
        continue
    m2 = re.match(r'^    (get|post|put|patch|delete):', l)
    if m2:
        cur_m = m2.group(1).upper()
        continue
    m3 = re.match(r'^      summary: "?([^"\n]+)"?', l)
    if m3 and cur_p and cur_m:
        ops.append((cur_m, cur_p, m3.group(1).strip()))
        cur_m = None

for m, p, s in ops:
    print(f'{m:6s} {p:50s} | {s}')
