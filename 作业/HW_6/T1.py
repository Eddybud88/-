import re

pattern = r'[bh][aiu]t'

test_strings = ['bat', 'bit', 'but', 'hat', 'hit', 'hut', 'cat']

matches = [s for s in test_strings if re.match(pattern, s)]

print(matches)
