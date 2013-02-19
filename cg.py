#!/usr/bin/env python
"""A Clebsh Gordan coefficient module"""

from math import sqrt, factorial
from fractions import Fraction
import numpy as np

def jrange(j1, j2):
    """Generator function looping over valid total angular momenta j"""
    j = abs(j1 - j2)
    while j <= j1 + j2:
        yield j
        j += 1

def mrange(j):
    """Generator function looping over valid total angular momentum projections m"""
    m = -j
    while m <= j:
        yield m
        m += 1

def inspect(f):
    def wrap(*args, **kwargs):
        print f.__name__, args, "=",
        result = f(*args, **kwargs)
        print result
        return result
    return wrap

#@inspect
def fac(arg):
    return factorial(int(arg))

def isodd(j):
    """Return True for odd integer input"""
    return j % 2 == 1

def iseven(j):
    """Return True for even integer input"""
    return j % 2 == 0

class cg:
    """ ClebshGordan class"""
    def __init__(self, j1, j2, j):
        self.j1 = j1
        self.j2 = j2
        self.j = j
        n1 = int(2*j1) + 1
        n2 = int(2*j2) + 1

        self.cgmat = np.zeros((n1, n2))
        jfac = sqrt(
            fac(j1+j2-j)*fac(j+j1-j2)*fac(j+j2-j1)*(2*j+1)
            /fac(j+j1+j2+1)
            )
        mj = list(mrange(j))
        for m1 in mrange(j1):
            p1 = int(j1 + m1)
            for m2 in mrange(j2):
                p2 = int(j2 + m2)
                m = m1 + m2
                if m in mj:
                    mfac = sqrt(fac(j1+m1)*fac(j1-m1)*fac(j2+m2)*fac(j2-m2)*fac(j+m)*fac(j-m))

                    kmin = int(max(0, -(j-j2+m1), -(j-j1-m2)))
                    kmax = int(min(j1+j2-j, j1-m1, j2+m2))
                    ksum = 0
                    for k in range(kmin, kmax+1):
                        ksum += (-1)**(k) / (
                              fac(k)*fac(j1+j2-j-k)*fac(j1-m1-k)*fac(j2+m2-k)
                              *fac(j-j2+m1+k)*fac(j-j1-m2+k)
                              )
                    self.cgmat[p1, p2] = jfac*mfac*ksum

    def __setitem__(self, m1, m2, val):
        p1 = int(self.j1 + m1)
        p2 = int(self.j2 + m2)
        self.cgmat[p1, p2]  = val

    def __getitem__(self, m1, m2):
        return self.cgmat[int(self.j1+m1), int(self.j2+m2)]

if __name__ == "__main__":
    """Output Clebsh Gordan matrix, input given as fractions"""
    import sys
    from fractions import Fraction
    try:
        a1 = sys.argv[1]
        a2 = sys.argv[2]
    except(IndexError):
        print "Usage:cg.py j1 j2"
        sys.exit(1)

    # Process input variables
    def halfint(a):
        j = Fraction(*map(int, a.split('/')))
        assert j.denominator == 2 or j.denominator == 1
        return j

    j1 = halfint(a1)
    j2 = halfint(a2)

    for j in jrange(j1, j2):
        j1, j2, j
        print cg(j1, j2, j).cgmat

