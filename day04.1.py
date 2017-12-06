f = open('./day04.txt', 'r')
lines = f.readlines()

count = 0
for line in lines:
  p = line.split()
  s = set(p)
  if len(p) == len(s):
    count += 1

print(count)
f.close()
