#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n < 2:
        return 1
    if n == 2:
        return n
    if cache and cache[n]:
        return cache[n]
    if not cache:
        cache = {i: 0 for i in range(n+1)}

    value = eating_cookies(n-1, cache) + eating_cookies(n-2,
                                                        cache) + eating_cookies(n-3, cache)
    cache[n] = value

    return value


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
