# -*- coding: utf-8 -*-
"""
https://learn.microsoft.com/en-us/bingmaps/rest-services/routes/calculate-a-route
"""
import json
import requests


bingmapskey = 'AuDeUjVAAIA1DDYQHh3RRbCl9eP2DEW35WSUkWUzlzDQWEUAHtHF2ybVQvV3oqvb'
wayPoint1 = 'Kazan'
viaWaypoint2 = 'Arsk'
waypoint3 = 'Kukmor'
waypointN = 'Sosnovka'
optimize = 'distance'
avoid = 'ferry,tolls'
routeAttributes = 'excludeItinerary'
maxSolutions = 2
distanceUnit = 'km'


# Find a driving route.
# \ - continue string to next line
url = f'http://dev.virtualearth.net/REST/v1/Routes/Driving?wayPoint.1={wayPoint1}\
        &viaWaypoint.2={viaWaypoint2} \
        &waypoint.3={waypoint3} \
        &wayPoint.n={waypointN} \
        &optimize={optimize} \
        &avoid={avoid} \
        &routeAttributes={routeAttributes} \
        &maxSolutions={maxSolutions} \
        &distanceUnit={distanceUnit} \
        &key={bingmapskey}'

api_request = requests.get(url)
if api_request.status_code == 200:
    result = json.loads(api_request.content)
    print(result)
else:
    print(api_request.status_code)

