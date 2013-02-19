from math import sqrt
import numpy as np
from fractions import Fraction as frac
from cg import cg

def assert_cg(ref, obj):
    print (obj.j1, obj.j2, obj.j)
    print ref 
    print obj.cgmat
    assert np.allclose(ref, obj.cgmat)

def test_ss():
    ref = [[1.0]]
    ss = cg.CG(0, 0, 0)
    assert_cg(ref, ss)

def test_sd():
    ref = [[1.0, 1.0]]
    h = frac(1, 2)
    sd = cg.CG(0, h, h)
    assert_cg(ref, sd)

def test_ds():
    ref = [[1.0], [1.0]]
    h = frac(1,2)
    ds = cg.CG(h, 0, h)
    assert_cg(ref, ds)

def test_dds():
    isq2 = sqrt(0.5)
    ref = [[0.0, -isq2], [isq2, 0.0]]
    h = frac(1, 2)
    dds = cg.CG(h, h, 0)
    assert_cg(ref, dds)

def test_ddt():
    isq2 = sqrt(0.5)
    ref = [[1.0, isq2], [isq2, 1.0]]
    h = frac(1,2)
    ddt = cg.CG(h, h, 1)
    assert_cg(ref, ddt)

def test_st():
    ref = [[1.0, 1.0, 1.0]]
    st = cg.CG(0, 1, 1)
    assert_cg(ref, st)

def test_ts():
    ref = [[1.0], [1.0], [1.0]]
    ts = cg.CG(1, 0, 1)
    assert_cg(ref, ts)

def test_tts():
    isq3 = sqrt(1.0/3.0)
    ref = [[0., 0., isq3], [0., -isq3, 0.], [isq3, 0., 0.]]
    tts = cg.CG(1, 1, 0)
    assert_cg(ref, tts)

def test_ttt():
    isq2 = sqrt(1.0/2.0)
    isq3 = sqrt(1.0/3.0)
    ref = [[0., -isq2, -isq2], [isq2, 0., -isq2], [isq2, isq2, 0.]]
    ttt = cg.CG(1, 1, 1)
    assert_cg(ref, ttt)

def test_ttq():
    isq2 = sqrt(1.0/2.0)
    isq3 = sqrt(1.0/3.0)
    isq6 = sqrt(1.0/6.0)
    ref = [[1., isq2, isq6], [isq2, 2*isq6, isq2], [isq6, isq2, 1.]]
    ttq = cg.CG(1, 1, 2)
    assert_cg(ref, ttq)

if __name__ == "__main__":
    test_dds()
