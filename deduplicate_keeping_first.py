# Need to install `llist` package for this to work
from llist import dllist
# Read in file from end to start

d = dllist()
with open('lineages.csv', 'r') as f:
    for line in f:
        d.append(line)

#%%
# Iterate over each line in d from back to front
# Save the string till first comma in hashset
# If string in hashset, delete line 
hashset = set()

keep_going=True
next = d.first
while next:
    current = next
    next = next.next
    line = current.value
    split = line.split(',')
    if line == '\n':
        d.remove(current)
        continue
    if split[0] in hashset:
        d.remove(current)
        print(f"Removed duplicate strain: {line}")
        continue
    hashset.add(split[0])
    

#%%
# Write back to file
with open('lineages.csv', 'w') as f:
    f.writelines(d)

