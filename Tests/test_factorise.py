from utils.q_e_factors import factorise


def test_factorise():
    assert factorise('x^2+2x+1') == ['x^2', '2x', '1']


def test_factorise2():
    assert factorise('x^3+2x^2+9x+12') == ['x^3', '2x^2', '9x', '12']
