# -*- coding: utf-8 -*-
"""
pip install SimConnect
"""

from SimConnect import *
from time import sleep

# Create SimConnect link
sm = SimConnect()
# Note the default _time is 2000 to be refreshed every 2 seconds
aq = AircraftRequests(sm, _time=2000)
# Use _time=ms where ms is the time in milliseconds to cache the data.
# Setting ms to 0 will disable data caching and always pull new data from the sim.
# There is still a timeout of 4 tries with a 10ms delay between checks.
# If no data is received in 40ms the value will be set to None
# Each request can be fine tuned by setting the time param.

# # To find and set timeout of cached data to 200ms:
# altitude = aq.find("PLANE_ALTITUDE")
# altitude.time = 200

# # Get the aircraft's current altitude
# altitude = aq.get("PLANE_ALTITUDE")
# altitude = altitude + 1000

# # Set the aircraft's current altitude
# aq.set("PLANE_ALTITUDE", altitude)

# ae = AircraftEvents(sm)
# # Trigger a simple event
# event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off
# event_to_trigger()

# # Trigger an event while passing a variable
# target_altitude = 15000
# event_to_trigger = ae.find("AP_ALT_VAR_SET_ENGLISH")  # Sets AP autopilot hold level
# event_to_trigger(target_altitude)

while not sm.quit:
    vs = aq.get("VERTICAL_SPEED")
    print(vs)
    sleep(1)

sm.exit()
quit()