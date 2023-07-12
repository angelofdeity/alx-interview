#!/usr/bin/python3
def minOperations(n):
    sumfactors = 0
    i = 2
    while i <= n:
        if not n % i:
            n /= i
            sumfactors += i
        else:
            i += 1
    return sumfactors
