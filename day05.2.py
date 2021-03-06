with open('./day05.txt', 'r') as f:
  arr = [int(x) for x in f.readlines()]

index = 0
steps = 0
while index < len(arr) and index >= 0:
  temp = index + arr[index]
  if arr[index] >= 3:
    arr[index] -= 1
  else:
    arr[index] += 1
  index = temp
  steps += 1

print(steps) # 28372145
