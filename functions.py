'''some functions for calculating profitable residential photovaltic data'''

def calc_self_consumption(consumption, capacity):
    '''calculates the self consumption'''
    production = capacity * 1000
    self_consumption = 0.3*production
    return self_consumption

def calc_feedin(capacity):
    return capacity * 0.3

def calc_crf(duration, rate):
    '''calcualtes the captial return factor '''
    crf=(pow((1+rate),duration)*rate)/(pow((1+rate),duration)-1)
    return crf

def calc_af(crf, invest):
    '''calculates the yearly annuität'''
    return invest*crf
def calc_cashflow(energy, tarif):
    return energy*tarif