#!/usr/bin/env python
def f(n):
   #print "n",n
   assert not isodd(n)
   return fac(n/2)

def fac(n):
   #print "n=",n
   assert n>=0
   assert type(n).__name__ == 'int'
   if n == 0:
      return 1
   else:
      return n*fac(n-1)

def triang(j1,j2,j):
   return j<=j1+j2 and j>=abs(j1-j2)

def nint(x):
   return int(x+0.5)

def isint(j):
   if abs(int(j)-j) < 1e-10:
      return 1
   else:
      return 0

def isodd(j):
   assert type(j).__name__ == 'int'
   if 2*(j/2) == j:
      return 0
   else:
      return 1

class cg:
   def __init__(self,j1,j2,m1,m2,j,m):
      self.j1=int(2*j1)
      self.j2=int(2*j2)
      self.m1=int(2*m1)
      self.m2=int(2*m2)
      self.j=int(2*j)
      self.m=int(2*m)
      self.data=self.calc()
   def __repr__(self):
      j1=self.j1
      j2=self.j2
      m1=self.m1
      m2=self.m2
      j=self.j
      m=self.m
      retstr = "<"
      pr=[]
      for i in (j1,j2,m1,m2,j,m):
         if i>=0: retstr+=" "
         if isodd(i):
            pr.append(i)
            retstr+=" %d/2"
         else:
            pr.append(i/2)
            retstr+= " %d"
      if self.data < 0: 
         retstr+=" > = %f"
      else:
         retstr+=" > =  %f"
      prt=tuple(pr+[self.data])
      return retstr % prt
   def __call__(self):
      return self.calc()
   def calc(self):
      from math import sqrt
      j1=self.j1
      j2=self.j2
      m1=self.m1
      m2=self.m2
      j=self.j
      m=self.m
      assert abs(m1) <= j1
      assert abs(m2) <= j2
      assert abs(m)  <= j
      #print j1,j2,m1,m2,j,m
      if m1+m2 == m and triang(j1,j2,j):
         _f=sqrt(
            1.0*f(j1+j2-j)*f(j+j1-j2)*f(j+j2-j1)*(j+1)
            /f(j+j1+j2+2)
            )
        #print "_f",_f
         kmin=max(0,-(j-j2+m1),-(j-j1-m2))
         kmax=min(j1+j2-j,j1-m1,j2+m2)
        #print "kmin=",kmin/2
        #print "kmax=",kmax/2
         _fsum=0
         for k in range(kmin,kmax+2,2):
           #print "k=",k/2
            _fsum+=(-1)**(k/2)*sqrt(
               f(j1+m1)*f(j1-m1)*f(j2+m2)*f(j2-m2)*f(j+m)*f(j-m)
               )/(
                 f(k)*f(j1+j2-j-k)*f(j1-m1-k)*f(j2+m2-k)
                 *f(j-j2+m1+k)*f(j-j1-m2+k)
                 )
        #print "_fsum",_fsum
         return _f*_fsum
      else:
         return 0.0
      
if __name__ == "__main__":
   #print "nint(0.6)=",nint(0.6)
   #print "nint(1.4)=",nint(1.4)
   #for i in range(6):
   #   print "%d!=%d" % (i,fac(i))
   import sys
   try:
      j1=float(sys.argv[1])
      j2=float(sys.argv[2])
   except IndexError:
      print "Usage: %s j1 j2"%sys.argv[0]
      sys.exit(-1)
   J1=int(2*j1)
   J2=int(2*j2)
   for J in range(J1+J2,abs(J1-J2)-1,-2):
      print ""
      j=.5*J
      for M in range(J,-J-1,-2):
         m=.5*M
         for M1 in range(J1,-J1-1,-2):
            m1=.5*M1
            m2=m-m1
            if abs(m2)>j2:
               pass
            else:
               print cg(j1,j2,m1,m2,j,m)
