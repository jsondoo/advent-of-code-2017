f = open('./day04.txt', 'r')
lines = f.readlines()

count = 0
for line in lines:
  passphrases = line.split()
  dicts = []
  for p in passphrases:
    dict = {}
    for c in p:
      if c in dict:
        dict[c] += 1
      else:
        dict[c] = 1
    dicts.append(dict)
  
  if len(set(frozenset(i.items()) for i in dicts)) == len(dicts):
    count += 1

print(count)
f.close()
