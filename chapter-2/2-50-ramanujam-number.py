from collections import defaultdict

def caches(n):
    return [i**3 for i in range(0, n)]

def ramanujam(n):
    cubes = caches(n)
    res = set()
    summap = defaultdict(set)
    
    for i in range(1, n):
        for j in range(i, n):
            if i == j:
                continue
            target = cubes[i] + cubes[j]
            newi, newj = min(i, j), max(i, j)
            if (newi, newj) in summap[target]:
                continue
            if len(summap[target]) != 0:
                res.add(target)
            summap[target].add((newi, newj))
    return list(sorted(res))

    '''
    for i in range(1, n):
        a = cubes[i]
        for j in range(n - 1, i, -1):
            target = a + cubes[j]
            #print(target)
            if target in res:
                continue
            l, r = i + 1, j - 1
            while l < r:
                other_target = cubes[l] + cubes[r]
                if other_target == target:
                    res.add(target)
                    break
                elif other_target > target:
                    r -= 1
                else:
                    l += 1
    '''
    return res

'''
Online implementation for testing correctness
'''
def RamanujamNumbersDP(n):
    numbers = []
    targets = set()
    Ds = dict()
    
    # Init List
    for d in range(0, n ** 3):
        Ds[d] = False
    
    # Fill list
    for d in range(0, n):
        Ds[d**3] = d

    for a in range(0, n):
        for b in range(0, n):
            for c in range(0, n):

                if a != b and a != c and b != c:
                    d = a ** 3 + b ** 3 - c ** 3

                    if a != d and b != d and c != d and d >= 0 and d < n ** 3:
                        if Ds[d] != False:
                            numbers.append((a, b, c, Ds[d]))
                            targets.add(a**3 + b**3)
                
    return list(sorted(targets))

#l1 = ramanujam(200)
#l2 = RamanujamNumbersDP(200)
#print(l1 == l2)
#print(f'n = 20 -> {ramanujam(20)}')
#print()
#print(f'n = 100 -> {ramanujam(100)}')
#print()
#print(f'n = 200 -> {ramanujam(200)}')
#print()
#print(f'n = 2000 -> {ramanujam(2000)}')
#print()
print(f'n = 20000 -> {ramanujam(20000)}')
print()
#print(f'n = 2000000 -> {ramanujam(2000)}')
