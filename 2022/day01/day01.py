import sys,os
os.chdir(os.path.dirname(sys.argv[0]))

def readlines(path:str):
    with open(path, 'r') as f:
        data =  [sum(list(map(int,row.split("\n")))) for row in f.read().split("\n\n")]
    return data


def solution1(location:str):
    calories=readlines(location)
    return sorted(calories)[-1]

def solution2(location:str):
    calories=readlines(location)
    return sum(sorted(calories)[-3:])

assert solution1("./data/test.txt")==24000
assert solution2("./data/test.txt")==45000

print(solution1("./data/data.txt"))
print(solution2("./data/data.txt"))

