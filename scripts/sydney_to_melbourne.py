"""
    Melbourne to sydney flight carbon cost

    Some information on this route is available here
    https://melbourneinfo.net.au/transport/flying-melbourne-to-sydney/

    Airplanes used:
        - Boeing 737-800 (QANTAS, VIRGIN)
        - Airbus A320 (JETSTAR)
        - Airbus A330-300 (QANTAS)
        - Airbus A330-200 (VIRGIN)

    Flight duration is roughly 1h35 mins
    Aerial distance is 718km


    Some reasonably high level information on Fuel economy for different aircraft here
    https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft

    Data below taken from regional flights section (926-1267km as the closest option)
    If no data in regional flights then it was taken from the short haul flights (1900km option)
    | AIRPLANE          | Fuel consumption per seat (L/100km)   |   Seats   |
    | Boeing 737-800    | 2.77                                  |   162     |
    | Airbus A320*      | 2.61                                  |   150     |
    | Airbus A330-300*  | 2.37                                  |   293     |
    | Airbus A330-200** | 3.11                                  |   241     |

    * short haul data
    * medium haul data  (probably don't use this)


    Info on carbon emission for jetfuel
    https://www.eesi.org/papers/view/fact-sheet-the-growth-in-greenhouse-gas-emissions-from-commercial-aviation

    3.16 kilograms CO2 per 1 kilogram of fuel consumed
    0.804kg/L density


    This worked out at roughly 50kg per seat.

    Interestingly there is this website that does a supposedly similar calculation
    https://co2.myclimate.org/en/portfolios?calculation_id=5086910
    and for this route it gives
    CO2 amount: 0.175 t

    which is a factor of 3 higher.

    So maybe I need to look into take off and landing amount?

    It goes into how it does the calculation here
    https://www.myclimate.org/fileadmin/user_upload/myclimate_-_home/01_Information/01_About_myclimate/09_Calculation_principles/Documents/myclimate-flight-calculator-documentation_EN.pdf
"""

distance = 718              # km
# distance = 3290              # km (Perth, jsut for comparison but probably should use different values for fuel economy)
jetfuel_density = 0.804     # kg/L
emission_factor = 3.16      # kg CO2 / kg fuel
carbon_cost = 48/1000       # $/kg (based on high prices reached this year)

fuel_economy_per_seat = {"Boeing 737-800": 2.77,
                         "Airbus A320": 2.61,
                         "Airbus A330-300": 2.37,
                         "Airbus A330-200": 3.11}

print("quick n dirty results for Sydney to Melbourne")
for plane, lp100 in fuel_economy_per_seat.items():
    litres_per_seat = distance/100*lp100
    kg_per_seat = litres_per_seat * jetfuel_density
    CO2_per_seat = kg_per_seat * emission_factor
    offset_cost = CO2_per_seat * carbon_cost
    print("Airplane {} emits {:.2f} kg CO2 per seat and cost ${:.2f} to offset".format(plane,CO2_per_seat, offset_cost))


