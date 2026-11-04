import re
from test_ddl_parser import tables

count_122 = 0
for tname, tdata in tables.items():
    for cname, con in tdata['constraints'].items():
        # normalize whitespace
        con_single = ' '.join(con.split())
        line = f'- `{con_single}`'
        if len(line) == 122:
            count_122 += 1
            print('122 line:', tname, repr(line))

print('Total 122 lines:', count_122)
