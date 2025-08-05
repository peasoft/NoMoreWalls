import re

with open("list.meta.yml", 'r') as file:
    content = file.read()
    lines = content.split("\n")
    for line_number in range(len(lines)):
        line = lines[line_number]
        if re.match(r'^\s*short-id', line):
           if not re.match(r'^\s*short-id: 7a2b', line):
               lines[line_number] = '    short-id: 6a2b'
               print(f"編輯第{line_number}行的節點short-id，從{line}到short-id: 7a2b")
    content_new = "\n".join(lines)
    file.close()

with open("list.meta.yml", 'w') as file:
    file.write(content_new)
