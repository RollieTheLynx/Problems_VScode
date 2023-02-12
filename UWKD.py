# -*- coding: utf-8 -*-
from functools import total_ordering
from my_keys import avaviationstack_key
import requests
import json
import pandas as pd


def load_page(offset, limit):
    try:
        api_request = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={avaviationstack_key}&arr_icao=UWKD&offset={offset}&limit={limit}")
        reply = json.loads(api_request.content)
    except Exception:
        reply = "Error..."
    if reply['pagination']['offset'] + reply['pagination']['count'] < reply['pagination']['total']:
        next_offset = reply['pagination']['offset'] + reply['pagination']['count']
    else:
        next_offset = None
    return reply['data'], next_offset


offset = 0
result = []

while offset is not None:
    data, offset = load_page(offset=offset, limit=100)
    result.extend(data)

df = pd.DataFrame.from_dict(result)
df['departure_iata'] = [d.get('iata') for d in df.departure]
df['company'] = [d.get('name') for d in df.airline]
df['flight_no'] = [d.get('icao') for d in df.flight]
print(df)
#df.to_excel('UWKD flights.xlsx', index=False)
