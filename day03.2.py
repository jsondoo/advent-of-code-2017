import numpy as np
import sys

grid = None
input = 277678

def main():
  global grid
  n = 101 # big enough to get answer
  grid = np.zeros((n+1,n+1)) # because screw zero-indexing

  mid = int((n+1)/2)
  grid[mid][mid] = 1

  x = mid + 1
  y = mid
  strip = 2
  while x >= 1 and x <= n and y >= 1 and y <= n:
    # going up 
    for i in range(strip):
      grid[y][x] = sumAround(y,x)
      y -= 1
    y += 1
    x -= 1
    # going left
    for i in range(strip):
      grid[y][x] = sumAround(y,x)
      x -= 1
    x += 1
    y += 1
    # going down
    for i in range(strip):
      grid[y][x] = sumAround(y,x)
      y += 1
    y -= 1
    x += 1
    # going right
    for i in range(strip):
      grid[y][x] = sumAround(y,x)
      x += 1
    strip += 2

def sumAround(row,col):
  global grid, input
  ans = grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1] + grid[row][col-1] + grid[row][col+1] + grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
  if ans > input:
    print(ans) # 279138
    sys.exit()
  else:
    return ans

main()
