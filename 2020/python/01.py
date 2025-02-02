import itertools, numpy

def solve(data, n):
    for nums in itertools.combinations(data, n):
        if sum(nums) == 2020:
            return numpy.prod(nums)

data = [ int(line.strip()) for line in open("../inputs/day01.txt", 'r') ]

print(solve(data, 2))
print(solve(data, 3))
