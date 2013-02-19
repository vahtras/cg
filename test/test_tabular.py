import numpy as np
from .. import cg

def assert_cg(ref, obj):
    print "<%d %d : : | %d - >"%(obj.j1, obj.j2, obj.j)
    print ref, obj.cgmat
    assert np.allclose(ref, obj.cgmat)

def test_ss():
    ref = [[1.0]]
    ss = cg.CG(0, 0, 0)
    assert_cg(ref, ss)
