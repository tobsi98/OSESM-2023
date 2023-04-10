'''functions for calculating the profitable of an residential photovaltic'''

def calc_self_consumption(consumption, capacity):
    '''calculates the self consumption
    assumptions:
    - yearly production capacity is 1000kWh/kWp, common for middle europe
    - self consumption rate is 30% , common for residential pv systems
    '''
    production = capacity * 1000
    self_consumption = 0.3*production
    return self_consumption

def calc_feedin(capacity):
    '''calculates the feed in energy
    assumptions:
    - self consumption rate is 30% , common for residential pv systems
    '''
    return capacity * 700

def calc_crf(duration, rate):
    '''calcualtes the captial return factor '''
    crf=(pow((1+rate),duration)*rate)/(pow((1+rate),duration)-1)
    return crf

def calc_af(crf, invest):
    '''calculates the yearly annuity'''
    return invest*crf
def calc_cashflow(energy, tarif):
    '''calculates the yearly cashflow'''
    return energy*tarif