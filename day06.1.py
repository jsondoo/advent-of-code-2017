answers = []

def getNext(x):
  arr = x.copy()
  biggest = arr[0]
  index = 0
  for i in range(len(arr)):
    if arr[i] > biggest:
      biggest = arr[i]
      index = i
  arr[index] = 0

  while biggest > 0:
    index = (index+1) % len(arr)
    arr[index] += 1
    biggest -= 1
  print(arr)
  return arr

def main():
  with open('./day06.txt', 'r') as f:
    data = f.read()
  arr = [int(x) for x in data.split()]
  # add initial configuration
  answers.append(arr)

  while True:
    next = getNext(arr)
    for a in answers:
      if next == a:
        print(len(answers)) # 5042
        return
    answers.append(next)
    arr = next

main()
