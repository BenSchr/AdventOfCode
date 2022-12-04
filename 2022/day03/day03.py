import sys,os
from string import ascii_letters
os.chdir(os.path.dirname(sys.argv[0]))

def split_string(row:str):
    first=row[:len(row)//2]
    second=row[len(row)//2:]
    return [first,second]

def readlines(path:str):
    with open(path, 'r') as f:
        data =  [row.strip() for row in f.readlines()]
    return data 

def calc_intersection(l:list,r:int):
    _set=set(l[0])
    for i in range(1,r):
        _set=_set.intersection(l[i])
    return ascii_letters.index(_set.pop())+1


def solution1(location:str):
    bags=readlines(location)    
    return sum([calc_intersection(split_string(bag),2) for bag in bags])

def solution2(location:str):
    bags=readlines(location)
    groups=[bags[x:x+3] for x in range(0,len(bags),3)]
    return sum([calc_intersection(group,3) for group in groups])

assert solution1("./data/test.txt")==157
assert solution2("./data/test.txt")==70

print(solution1("./data/data.txt"))
print(solution2("./data/data.txt"))

