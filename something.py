import numpy as np

def dice_rolls(n):
    print (f'The results of {n} dice rolls are:')
    return np.random.randint(1,7,n)

def d20_dice_rolls(n):
    return np.random.randint(1,21,n)

print (1)
