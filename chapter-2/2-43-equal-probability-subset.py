def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def comb(n, k):
    if n == 0 or k == 0:
        return 1
    return fact(n) // (fact(n - k) *  fact(k))

'''
Problem -> How to generate a random subset of size k from an array of size n with only one-pass

Solution -> There are nCk subsets. When arranged in sorted order, let's consider a set of first n natural numbers - {1,2, 3, 4,...,n}

Arranging all subsets of size k in ascending order -> There are n-1Ck-1 subsets starting with 1. The subsequent n-2Ck-2 start with 2. Then the next n-3Ck-3 start with 3 and so on.
Within the first n-1Ck-1 that start with 1, the number of subsets that start with 1,2 as first two elements is n-2Ck-2, number starting with 1,3 is n-3Ck-3
Within the first n-2Ck-1 that start with 2, the number of subsets that start with 2, 3 is n-3Ck-2, number starting with 2,4 is n-4Ck-3
With first n-3Ck-1 start with 3, {3,4} is n-4Ck-2, {3,5} is n-5Ck-2 and so on.

So with some intelligent counting, it becomes possible to get the nth unique subset without generating all nCk subsets

Time Complexity: O(n^2) since nCk is O(n) and while loop runs atmost n times
'''
def get_random_subset(n, k, setnum):
    total_subsets = comb(n, k)
    subset = []
    if setnum < 0 or setnum > total_subsets:
        return subset
    i = 1 # The first element or the first index to sample
    while k > 0:
        #print(f'n now {n}, k now {k}, subset now {subset}')
        cur_bucket = comb(n - 1, k - 1)
        #print(f'setnum is {setnum}, cur_bucket is {cur_bucket}')
        if setnum <= cur_bucket:
            subset.append(i)
            k -= 1
        else:
            setnum -= cur_bucket
        n -= 1
        i += 1 
    return subset

print(get_random_subset(3, 2, 3))
print(get_random_subset(5, 3, 2))
print(get_random_subset(5, 3, 4))
print(get_random_subset(5, 3, 9))
print(get_random_subset(5, 3, 10))
print(get_random_subset(5, 3, 11))
