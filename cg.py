#!/usr/bin/env python
"""A Clebsh Gordan coefficient module"""

__version__ = "1.0"

import sys
from math import sqrt, factorial
from fractions import Fraction
import numpy as np

def mrange(j):
    """
    Generator function: given total angmular momentum j,
    loop over valid total angular momentum projections |m|<=j
    """
    m = -j
    while m <= j:
        yield m
        m += 1

def fac(arg):
    """Factorial of numbers of Fraction type"""
    return factorial(int(arg))

class CG(object):
    """ ClebshGordan class"""
    def __init__(self, j1, j2, j):
        self.j1 = j1
        self.j2 = j2
        self.j = j
        n1 = int(2*j1) + 1
        n2 = int(2*j2) + 1

        self.cgmat = np.zeros((n1, n2))
        self.set_matrix()

    def set_matrix(self):
        """Calculate transformation matrix"""

        j1 = self.j1
        j2 = self.j2
        j = self.j

        for m1 in mrange(j1):
            p1 = int(j1 + m1)
            for m2 in mrange(j2):
                p2 = int(j2 + m2)
                m = m1 + m2
                if m in mrange(j):
                    mfac = sqrt(
                        fac(j1+m1)*fac(j1-m1)*fac(j2+m2)*\
                        fac(j2-m2)*fac(j+m)*fac(j-m)
                        )

                    kmin = int(max(0, -(j-j2+m1), -(j-j1-m2)))
                    kmax = int(min(j1+j2-j, j1-m1, j2+m2))
                    ksum = 0
                    for k in range(kmin, kmax+1):
                        ksum += float((-1)**(k)) / (
                              fac(k)*fac(j1+j2-j-k)*fac(j1-m1-k)*fac(j2+m2-k)
                              *fac(j-j2+m1+k)*fac(j-j1-m2+k)
                              )
                    self.cgmat[p1, p2] = mfac*ksum

        self.cgmat *= self.jfac()

    def jfac(self):
        """
        Factor of j-values in cg-coefficient
        """

        j1 = self.j1
        j2 = self.j2
        j = self.j
        return sqrt(
            float(fac(j1+j2-j)*fac(j+j1-j2)*fac(j+j2-j1)*(2*j+1))
            /fac(j+j1+j2+1)
            )

    def __setitem__(self, m1, m2, val):
        p1 = int(self.j1 + m1)
        p2 = int(self.j2 + m2)
        self.cgmat[p1, p2] = val

    def __getitem__(self, m1, m2):
        return self.cgmat[int(self.j1+m1), int(self.j2+m2)]


class HalfInt(Fraction):
    def __init__(self, *args):
        try:
            super(HalfInt, self).__init__(*args)
        except TypeError:
            super().__init__()
        #Fraction.__init__(*args)
        if self.denominator > 2:
            raise ValueError('invalid literal for HalfInt: %s' % str(args))

def main():
    try:
        a1 = sys.argv[1]
        a2 = sys.argv[2]
        a3 = sys.argv[3]
    except IndexError:
        print("Usage:cg.py j1 j2 j")
        sys.exit(1)

    # Process input variables

    j_1 = HalfInt(a1)
    j_2 = HalfInt(a2)
    j_tot = HalfInt(a3)

    print(CG(j_1, j_2, j_tot).cgmat)

if __name__ == "__main__":
    sys.exit(main())
