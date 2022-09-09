"""
There's 150 flights per day between melbourne and sydney:
https://melbourneinfo.net.au/transport/flying-melbourne-to-sydney/


An "average" flight emits
>>> (50.53+47.61+43.23+56.73)/4
49.525 kg per seat of CO2

An average flight has
>>> (162+150+293+241)/4
211.5 seats

The "average flight emits:
>>> 211.5*49.525
10474 kg per flight CO2
or
10.5 tonnes/flight

Per day, thats
>>> 10.5*150
1575 tonnes/day

Per year, thats:
>>>10.5*150*365
574875.0 tonnes/year CO2

~ 575 Mt/year

Assuming
carbon_cost = 48 $/ton

>>>574875*48
27594000

$27 million per year
or
$74,000 per day
"""




