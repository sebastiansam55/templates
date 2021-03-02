import re


### re.sub
def replacement(match):
    return "test"

data = """
this is not
a test of the 
"""
#re.sub(pattern, replacement, data, count=0)
print(re.sub(r't', replacement, data))
# replacement can be a string or a method that returns one and takes one match object argument.

### re.findall
data = "this is a list a item to find all"

pat = r't|a|l'
matches = re.findall(pat, data)

print(matches)

### re.finditer
# like findall but returns a iterable that can be used in a loop

for item in re.finditer(pat, data):
    print(item)
