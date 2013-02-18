#!/usr/bin/env python
"""A Clebsh Gordan coefficient module"""
def fh(n):
    """Return factorial for half value"""
    from math import factorial
    return factorial(n/2)

def isodd(j):
    """Return True for odd integer input"""
    return j % 2 == 1

def iseven(j):
    """Return True for even integer input"""
    return j % 2 == 0

class cg:
    """ ClebshGordan class"""
    def __init__(self, j1, j2, m1, m2, j, m):
        self.j1 = int(2*j1)
        self.j2 = int(2*j2)
        self.m1 = int(2*m1)
        self.m2 = int(2*m2)
        self.j = int(2*j)
        self.m = int(2*m)
        self.data = self()
    def __repr__(self):
        j1 = self.j1
        j2 = self.j2
        m1 = self.m1
        m2 = self.m2
        j = self.j
        m = self.m
        retstr = "<"
        pr = []
        for i in (j1, j2, m1, m2, j, m):
            if i >= 0 : retstr += " "
            if isodd(i):
                pr.append(i)
                retstr += " %d/2"
            else:
                pr.append(i/2)
                retstr += " %d"
        if self.data < 0: 
            retstr += " > = %f"
        else:
            retstr += " > =  %f"
        prt = tuple(pr+[self.data])
        return retstr % prt

    def __call__(self):
        """Callable object"""
        from math import sqrt
        j1 = self.j1
        j2 = self.j2
        m1 = self.m1
        m2 = self.m2
        j = self.j
        m = self.m
        assert abs(m1) <= j1
        assert abs(m2) <= j2
        assert abs(m)  <= j
        #print j1,j2,m1,m2,j,m
        if m1+m2 == m and abs(j1-j2) <= j <= j1+j2:
            _f = sqrt(
                1.0*fh(j1+j2-j)*fh(j+j1-j2)*fh(j+j2-j1)*(j+1)
                /fh(j+j1+j2+2)
                )
           #print "_f",_f
            kmin = max(0, -(j-j2+m1), -(j-j1-m2))
            kmax = min(j1+j2-j, j1-m1, j2+m2)
           #print "kmin=",kmin/2
           #print "kmax=",kmax/2
            _fsum = 0
            for k in range(kmin, kmax+2, 2):
               #print "k=",k/2
                _fsum += (-1)**(k/2)*sqrt(
                    fh(j1+m1)*fh(j1-m1)*fh(j2+m2)*fh(j2-m2)*fh(j+m)*fh(j-m)
                    )/(
                      fh(k)*fh(j1+j2-j-k)*fh(j1-m1-k)*fh(j2+m2-k)
                      *fh(j-j2+m1+k)*fh(j-j1-m2+k)
                      )
           #print "_fsum",_fsum
            return _f * _fsum
        else:
            return 0.0
      
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

    J1 = int(2*j1)
    J2 = int(2*j2)

    for J in range(J1+J2, abs(J1-J2)-1, -2):
        print ""
        j = .5*J
        for M in range(J, -J-1, -2):
            m = .5*M
            for M1 in range(J1, -J1-1, -2):
                m1 = .5*M1
                m2 = m-m1
                if abs(m2) > j2:
                    pass
                else:
                    print cg(j1, j2, m1, m2, j, m)
