# -*- coding: utf-8 -*-
"""
Downloads and interprets METAR weather report for a specified aiport

@author: Rollie

https://metar-taf.com/explanation
"""
import requests
import pandas as pd
import re

def get_metar(icao):
    url = f"https://beta.aviationweather.gov/cgi-bin/data/metar.php?ids={icao}"
    try:
        api_request = requests.get(url)
        response = api_request.content
        metar = response.decode('UTF-8')
    except Exception:
        metar = "Error..."
    return metar


def parse_metar(metar):
    def find_type(input_text):
        pattern = re.compile(r"\b(?:METAR|TAF|SPECI)\b", re.IGNORECASE)
        type_part = pattern.match(input_text)
        return type_part.group(0) if type_part is not None else None
    
    def find_icao(input_text):
        icao_part = input_text.split()[1] if type_part is not None else input_text.split()[0]
        return icao_part
    
    def find_time(input_text):
        match = re.search(r'\b(\w*[Zz])\b', input_text)
        time_part = match.group() if match is not None else None
        return time_part

    def find_corautonil(input_text):
        pattern = re.compile(r"\b(?:COR|AUTO|NIL)\b", re.IGNORECASE)
        corautonil_part = pattern.match(input_text)
        return corautonil_part.group(0) if corautonil_part is not None else None

    def find_wind(input_text):
        match = re.search(r'\b(?:\w*[KT|MPS|MPH])\b', input_text)
        wind_part = match.group() if match is not None else None
        return wind_part
    
    def find_windvar(input_text):
        match = re.search(r'\b(?:\d*V\d*)\b', input_text)
        windvar_part = match.group() if match is not None else None
        return windvar_part

    def find_visibility(input_text):
        list_of_words = input_text.split()
        # if there is no windvar, visibility goes next after wind_part, else second next after wind_part
        visibility_part = list_of_words[list_of_words.index(wind_part) + 1] if windvar_part is None else list_of_words[list_of_words.index(wind_part) + 2]
        return visibility_part
    
    def find_temp(input_text):
        match = re.search(r'\bM?+[0-9]+[\/]+M?+[0-9]+\b', input_text)
        temp_part = match.group() if match is not None else None
        return temp_part
    
    def find_pressure(input_text):
        match = re.search(r'\b[A|Q][0-9]{4}\b', input_text)
        pressure_part = match.group() if match is not None else None
        return pressure_part

    
    type_part = find_type(metar)
    icao_part = find_icao(metar)
    time_part = find_time(metar)
    corautonil_part = find_corautonil(metar)
    wind_part = find_wind(metar)
    windvar_part = find_windvar(metar)
    visibility_part = find_visibility(metar)
    temp_part = find_temp(metar)
    pressure_part = find_pressure(metar)

    return (type_part, icao_part, time_part, corautonil_part, wind_part,
            windvar_part, visibility_part, temp_part, pressure_part)


def interpret_type(type_part):
    # Indicates whether it is a planned sighting METAR or intermediate sighting (SPECI).
    # The SPECI is not much used anymore because most weather stations issue a new observation every half hour.
    match type_part:
        case "METAR":
            print(f'{type_part}: type of report is a planned sighting METAR (Meteorological Aerodrome Report)')
        case "TAF":
            print(f'{type_part}: type of report is TAF')
        case "SPECI":
            print(f'{type_part}: type of report is a nonroutine aviation special weather report')
        case _: # else
            pass


def interpret_icao(icao_part):
    # The ICAO code of the airport / weather station. Usually this is a 4 letter code.
    # Example: EHLE stands for Lelystad Airport.
    airports = pd.read_csv("UWKD\\airport_code.csv")
    airport_name = airports.loc[airports['ident'] == icao_part, ['name']].iloc[0]['name']
    print(f'{icao_part}: ICAO code of airport {airport_name}')
        

def interpret_time(time_part): 
    # The first 2 digits indicate the day of the month.
    # Followed by the 2 digits of the hour (00-23) and the minutes (00-59).
    # Z is the abbreviation for Zero, time zone 0 is Greenwich Mean Time (UTC).
    # In the NATO phonetic alphabet, the Z is pronounced Zulu, which is why it is also called Zulu time.
    # Note that both the day and time are displayed in UTC / zulu time.
    # This is done to avoid misunderstandings.
    # So 280925Z means the 28th day of the month at 09:25 UTC. 
    local_hour = int(time_part[2:4]) + 3
    if local_hour > 24:
        local_hour -= 24
        local_hour = '0' + str(local_hour)
    print(f'{time_part}: {time_part[0:2]}th day of current month and {time_part[2:4]}:{time_part[4:6]} zulu, or UTC time ({local_hour}:{time_part[4:6]} in Moscow)')
  

def interpret_corautonil(corautonil_part):
    # COR means that this observation replaces a previously drawn up report.
    # AUTO means that the observation is done automatically. Automatic observations are more limited than manually generated observations.
    # NIL means that no data is known.
    match corautonil_part:
        case "COR":
            print(f'{corautonil_part}: means that this observation replaces a previously drawn up report')
        case "AUTO":
            print(f'{corautonil_part}: means that the observation is done automatically')
        case "NIL":
            print(f'{corautonil_part}: means that no data is known')
        case _: # else
            pass
        

def interpret_wind(wind_part):
    # 10009G19KT 060V130 means that the mean wind direction is 100°, variable between 60 and 130°.
    # The average wind speed is 9 knots (09) with peaks up to 19 knots (KT).
    if 'VRB' in wind_part:
        direction = 'variable'
    else:
        direction = wind_part[0:3] + '\u00B0'

    speed = wind_part[3:5]

    if 'MPS' in wind_part:
        unit = 'm/s'
    elif 'KT' in wind_part:
        unit = 'knots'
    elif 'MPH' in wind_part:
        unit = 'm/h'

    if 'G' in wind_part:
        gust_speed = wind_part.split('G', 1)[1][0:2]
        gusts = f' with gusts up to {gust_speed} {unit}'
    else:
        gusts = ''

    if '/////' in wind_part:
        print(f'{wind_part}: wind direction cannot be determined')
    else:
        print(f'{wind_part}: wind direction is {direction} and speed is {speed} {unit}{gusts}')
        

def interpret_windvar(windvar_part):
    if windvar_part is not None:
        print(f'{windvar_part}: wind direction varies between {windvar_part[0:3]} and {windvar_part[4:7]}\u00B0')


def interpret_visibility(visibility_part):
    # The visibility shown in the METAR is an average, minimum visibility.
    # 5000 means visibility is 5000 meters.
    # If visibility is less than 1000 meters, the number will be added to 4 characters.
    if 'CAVOK' in visibility_part:
        visibility = 'Ceiling and visibility are OK'
    elif 'SM' in visibility_part:
        if '/' in visibility_part:
            num,den = visibility_part[0:-2].split( '/' )
            meters = float(num)/float(den)*1609.344
        else:
            meters = float(visibility_part[0:-2])*1609.344
        visibility = f'Visibility is {visibility_part[0:-2]} statute miles ({round(meters)} meters)'
    else:
        visibility = f'Visibility is {visibility_part} meters'

    print(f'{visibility_part}: {visibility}')
    

def interpret_temp(temp_part):
    # 02/M01 means that the temperature is 2 °C and the dew point is -1 °C. Negative numbers are preceded by an M.
    temp = '-' + temp_part[1:3] if temp_part[0] == 'M' else '+'+ temp_part[0:2]
    dew_sign = '-' if '/M' in temp_part else '+'
    print(f'{temp_part}: the temperature is {temp}\u00B0C and the dew point is {dew_sign}{temp_part[-2:]}\u00B0C')

    
def interpret_pressure(pressure_part):
    # In the METAR you will also find the air pressure at the mean sea level (QNH).
    # This is calculated by recalculating the air pressure at terrain height (QFE) back to sea level.
    # Air pressure can be expressed in inches of mercury (preceded by an A) or hectopascals (preceded by a Q).
    # A2994 means air pressure of 29.94 inHg.
    # Q1001 means an air pressure of 1001 hPa.
    pressure_unit = 'inHg' if pressure_part[0] == 'A' else 'hPa'
    print(f"{pressure_part}: the pressure is {pressure_part[1:]} {pressure_unit}")


# icao = "UWKD"
# metar = get_metar(icao)
metar = 'METAR UWKD 122230Z COR 19004G10MPH 060V130 1/2SM 08/M05 Q1016 R29/CLRD70 NOSIG RMK QFE751/1001'
print("METAR is:")
print(metar)

(type_part, icao_part, time_part, corautonil_part, wind_part,
 windvar_part, visibility_part, temp_part, pressure_part) = parse_metar(metar)

interpret_type(type_part)
interpret_icao(icao_part)   
interpret_time(time_part)
interpret_corautonil(corautonil_part)
interpret_wind(wind_part)
interpret_windvar(windvar_part)
interpret_visibility(visibility_part)
interpret_temp(temp_part)
interpret_pressure(pressure_part)


# TODO Visibility can be different in different directions. In that case the lowest measured visibility is always displayed. If visibility is only measured in one direction then NDV (Non Directional Variation) is added to the code.
# Visibility can also be listed per direction. 1500SW 2000NE means the visibility to the southwest is 1500 meters and 2000 meters to the northeast.
# In case of poor visibility, the direction can also be displayed per runway. This is also called the RVR (Runway Visual Range). An RVR is usually not reported until visibility is less than 2000 meters. Examples of an RVR:
# R23/0500 visibility for runway 23 is 500 meters
# R23/P0500 visibility for runway 23 is more (P) than 500 meters
# R23/M0500 visibility for runway 23 is less (M) than 500 meters
# R23/0500V1500 visibility for runway 23 varies between 500 and 1500 meters
# R23/0500U visibility for runway 23 is 500 meters but increases (U)
# R23/0500D visibility for runway 23 is 500 meters but decreases (D)