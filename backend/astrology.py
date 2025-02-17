import swisseph as swe
from datetime import datetime

def calculate_lagna(data):
    date, time, lat, lon = data["date"], data["time"], data["lat"], data["lon"]
    dt = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    julian_day = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60.0)
    
    planets = [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER, swe.VENUS, swe.SATURN, swe.RAHU, swe.KETU]
    chart = {swe.get_planet_name(p): swe.calc_ut(julian_day, p)[0][0] for p in planets}
    return chart

def vimshottari_dasa(data):
    return {"message": "Vimshottari Dasa calculations coming soon!"}

def kp_astrology(data):
    return {"message": "KP Astrology calculations coming soon!"}
