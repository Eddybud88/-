import re

s = "我出生时间为1990-01-01 00:00:00,今天时间为2019-04-20 12:20:00"
pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
matches = re.findall(pattern, s)
print(matches)
