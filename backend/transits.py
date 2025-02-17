import swisseph as swe
from datetime import datetime

def get_transits(data):
    date = data["date"]
    dt = datetime.strptime(date, "%Y-%m-%d")
    julian_day = swe.julday(dt.year, dt.month, dt.day)

    transits = {}
    for planet in [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER, swe.VENUS, swe.SATURN]:
        pos, _ = swe.calc_ut(julian_day, planet)
        transits[swe.get_planet_name(planet)] = pos[0]

    return transits
