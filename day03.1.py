# No coding needed, look for patterns

# Notice that the bottom right square corner are the squares of odd numbers 1^2 3^2 5^2 ...
# My input was 277678
# Closest odd square is 527*527 = 277729
# In this row there are 527 numbers
# So in the middle of this row the number is 277466 = 277729 - (527-1)/2
# Distance from my input 277678 to 277466 is 212
# Distance from middle of this row to access port is 263 (since this is the 264th row, since (527+1)/2=264)
# Total manhattan distance = 212 + 263 = 475
