import functions
import math

def test_calc_self_consumption():
    assert functions.calc_self_consumption(10000,10)==2000
def test_calc_feedin():
    assert functions.calc_feedin(10) == 7000
def test_calc_crf():
    assert math.isclose(functions.calc_crf(10,10),10,abs_tol = 0.001)
def test_calc_af():
    assert functions.calc_af(0.3,1000)== 200
def test_calc_cashflow():
    assert functions.calc_cashflow(10000,0.5) == 5000
