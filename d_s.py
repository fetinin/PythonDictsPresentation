#!/usr/bin/python2.7

def calc_idx(key, n):
    i = hash(key) % n
    yield i
    perturb = hash(key)
    while True:
        i = (5 * i + perturb + 1) % n
        print "Perturb is", perturb
        perturb >>= 5
        yield i