# Hashsets
s = set()
print(s)

# Add item into set - O(1)

s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item is in the set -O(1)

if 1 in s:
    print(True)
else:
    print(False)

s.remove(3)
print(s)

 # Set construction - O(S) - S is the length of the string

string = 'asdfasasdfasdsadfsasdfsa'
sett = set(string)

print(sett)

# loop over items in set - O(n)

for i in sett:
    print(i)

# Hashmaps - Dictionaries

dic = {
    'nadeem': ['aluva', 'panangad'],
    'nandu': 'edapally',
    'christy': 'nettoor',
    'anand': 'vypin',
    'ahzan': 'panayikulam',
}
print(dic)

# Add key:value pair in dictionary: O(1)

dic['robin'] = 'kollam'
print(dic)

# Check for presence of a key in dictionary: O(1)

if 'anand' not in dic:
    print(True)
else:
    print(False)

#  Check value corresponding to a key in dictionary: O(1)
print(dic['anand'])

# Loop over a dictionary: O(n)

for key, value in dic.items():
    print(f'{key}: {value}')

# Default dict

from collections import defaultdict
default = defaultdict(list)
default[2]
print(default)

# Counter

from collections import Counter

counter = Counter(string)
print(counter)