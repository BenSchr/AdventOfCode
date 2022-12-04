import sys,os
os.chdir(os.path.dirname(sys.argv[0]))

_map={
    "A":1, # Rock
    "B":2, # Paper
    "C":3, # Scissor
    "X":1, # Lose
    "Y":2, # Draw
    "Z":3  # Win
}     

def apply_map(value:str):
    return _map[value]

def readlines(path:str):
    with open(path, 'r') as f:
        data =  [tuple(map(apply_map,row.split())) for row in f.readlines()]
    return data

def score(one,two):
    if ((one % 3) + 1 == two):  #Win
        return two+6
    elif((two % 3) + 1 == one): #Lose
        return two+0
    else:                       #Draw 
        return two+3       

def solution1(location:str):
    rounds=readlines(location)    
    return sum([score(one,two) for one,two in rounds])

def solution2(location:str):
    rounds=readlines(location)
    strategy=[(one,(((one+two)%3)+1)) for one,two in rounds]
    return sum([score(one,two) for one,two in strategy])

assert solution1("./data/test.txt")==15
assert solution2("./data/test.txt")==12

print(solution1("./data/data.txt"))
print(solution2("./data/data.txt"))

