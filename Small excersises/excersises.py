campaign_name = "LatAm ENG Search New"

# Your original (incorrect) code:
print(('US' or 'LatAm') in campaign_name)  # False - because it's checking if 'US' is in "LatAm ENG Search New"

# Correct code:
print('US' in campaign_name or 'LatAm' in campaign_name)  # True - correctly finds 'LatAm'