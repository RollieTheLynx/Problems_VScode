"""
Remove emoji from a text file and print it to stdout.
Usage
-----
    python remove-emoji.py input.txt > output.txt
"""
import re
import sys

# https://stackoverflow.com/a/49146722/330558
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

if __name__ == '__main__':
    text = """FAMILY RESIDENTIAL COMPLEX "BANUEVLERI BAHÇEKENT" (ESENYURT, ISTANBUL) ⚜️

BANUEVLERI BAHÇEKENT is one of the most comfortable family-type residential projects in the Bahçekent neighborhood (Esenyurt, Istanbul), bordering the Bahçeşehir neighborhood. The project is located next to other modern residential projects. The complex offers 2 types of spacious and comfortable apartments, designed in a modern architectural style. The complex includes a spacious courtyard, playgrounds and playgrounds, and a range of social and sports services.

The location is convenient and has a solid investment potential. The peculiarity of the location of the project is, on the one hand, the inhabited character of the area, in which schools, kindergartens, universities, hospitals, clinics, cafes, restaurants and other social infrastructure facilities have been operating for many years, on the other hand, active infrastructure development continues near the project, including, first of all, we are talking about the construction of the Istanbul Canal, a mega-infrastructure project of the 21st century. The opening in 2022 of the Marmaray high-speed intra-city railway station near the project location and the active construction of the metro station also testify to the high importance attached by the city authorities to the infrastructure development of this area.

The author of the project is one of the leading developers in Turkey – the construction group "Hasanoğlu", which has 30 years of experience in construction and dozens of construction projects in Istanbul, both in the residential sector and in the construction of infrastructure facilities.

📌 PROJECT CHARACTERISTICS

▫️Project area: 9,271 m²
▫️Number of buildings: 2 🏙️
▫️Stories of buildings: 11 🏙️
▫️Number of apartments: 84
▫️Types of apartments: 2+1 (42 pcs.) and 3+1 (42pcs.)
▫️Net areas of apartments: 104–137 m²
▫️Building material: concrete frame, red brick 🧱
▫️Gas supply 🔥
▫️Start of construction: December 2022 📅
▫️Completion date: December 2024 📅

📌 EXTERNAL INFRASTRUCTURE

▫️E80 Trans-European Motorway (TEM) – 2 min 🚘🛣️
▫️North Marmara Motorway – 15 min 🚘🛣️
▫️Istanbul International Airport – 25 min ✈️
▫️Public transport stop – 0.5 min 🚌
▫️Speed urban railway "Marmaray" – 10 min 🚝
▫️Metropolitan (under construction) – 10 min 🚇
▫️Sanatorium and health complex with thermal springs MidIstanbul - 10 min 🫧🌞
▫️Shop "File" - 1 min 🛒
▫️Shop "Migros" - 2 min 🛒
▫️Shop "BIM" - 2 min 🛒
▫️Shop "SHOCK" - 3 min 🛒
▫️Akbaty Mall – 10 min 🎁🛍️🛒
▫️Cultural College 2000 – 9 min 🎓
▫️Elite International Schools:
       ▫️Al-Mawakeb – 10 min 🎓
       ▫️Gökkuşağı - 5 min 🎓
▫️Universities:
    ▫️Beykent University – 6 min 🎓
    ▫️Istanbul University (Jerrahpasha) – 8 min 🎓
▫️Istinye University Hospital – 12 min 🏥
▫️A huge public park with a pond, with sports and playgrounds, gazebos, a picnic area – 2 min 🌳☘️
▫️2 mosques: 2 and 5 min 🕌
▫️Many other social infrastructure facilities in the immediate vicinity: schools, colleges, lyceums, kindergartens, clinics, a notary's office, language courses, service departments, etc.

📌 INTERNAL INFRASTRUCTURE

▫️7 commercial objects (cafes, shops, etc.) 🛍️🛒🍿
▫️Fitness Gym 🤸‍♀️🏋🏻‍♂️🚴🏿‍♂️
▫️Hamam, sauna 🛀🧼
▫️Sports ground ⛹🏼
▫️Playgrounds 🛝
▫️Gardens, green spaces 🌳
▫️Picnic areas 🌭🫕
▫️Walking paths 🚶🏻
▫️Individual depot (luggage storage) 📦
▫️Underground parking (1-2 cars) 🚘
▫️Guest parking 🚘
▫️24 hour security 🚔⚔️👮🏻‍♂️
▫️Video surveillance 📹
▫️Prayer room 🕌

📌 OTHER INFORMATION

▫️Ready title deed 📜
▫️Title deed fee – 2% 📜💵
▫️Suitable for Turkish citizenship 🇹🇷"""
    #text = open(sys.argv[1]).read()
    text = remove_emoji(text)
    print(text)