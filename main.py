import functions

duration = 10
rate = 0.01
installed_capacity = 10
price_i = 1000
consumption = 3000
tarif_feedin = 0.2
tarif_supply= 0.4

sc = functions.calc_self_consumption(consumption,installed_capacity)
fd = functions.calc_feedin(installed_capacity)

invest = installed_capacity * price_i
crf= functions.calc_crf(duration,rate)
a = functions.calc_af(crf,invest)
earnings = functions.calc_cashflow(sc,tarif_supply) + functions.calc_cashflow(fd,tarif_supply)
if (a < earnings):
    print("The PV is an profitable investement: with " + str(earnings) + "€ per year")