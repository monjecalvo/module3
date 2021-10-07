blocks = int(input("Number of blocks "))
height = 0
layerblocks = 1

while layerblocks <= blocks:
    height += 1
    blocks -= layerblocks
    layerblocks += 1

print("The height is", height)    
