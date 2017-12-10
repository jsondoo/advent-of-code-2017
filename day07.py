class Node:
  def __init__(self, name, val):
    self.name = name
    self.val = val
    self.children = []

  def add_children(self, node):
    self.children.append(node)

  def count_children(self):
    count = len(self.children)
    for c in self.children:
      count += c.count_children()
    return count

  def get_weight(self):
    weight = self.val
    for c in self.children:
      weight += c.get_weight()
    return weight

with open('./day07.txt', 'r') as f:
  data = [line.rstrip('\n') for line in f]

# map node name to node
dict = {}

# make one pass and create the nodes without children
for d in data:
  a = d.split() # a[0] = name, a[1] = (val), a[2] = ->, a[3...] = children names
  n = a[0]
  v = int(a[1][1:-1])
  temp_node = Node(n,v)
  dict[n] = temp_node

# make another pass and add children
for d in data:
  a = d.split() # a[0] = name, a[1] = (val), a[2] = ->, a[3...] = children names
  node = dict[a[0]]
  if len(a) >= 4:
    for i in range(3,len(a)):
      node.add_children(dict[a[i].rstrip(',')])

# make another pass and find node with most children
maxi = 0
top_node = None
for key,val in dict.items():
  if dict[key].count_children() > maxi:
    maxi = dict[key].count_children()
    top_node = dict[key]

print(top_node.name) # PART 1 : gmcrj

# BFS down from top_node until you see an unbalanced disc
def bfs(node):
  if not a:
    return

  arr = []
  for c in node.children:
    arr.append(c.get_weight())
  
  if arr and not check_all_same(arr):
    print(node.name, arr) 
    # look at this output and deduce the weight that needs to be changed
    # mdbtyw needs to be 5 lighter

  for c in node.children:
    bfs(c)

def check_all_same(arr):
  first = arr[0]
  for i in range(len(arr)):
    if arr[i] != first:
      return False
  return True


bfs(top_node)

  