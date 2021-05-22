'''
Считывает файлы GPX и фотографии с геометками и создает HTML с вашмим туром!
'''
from xml.dom import minidom
from exif import Image
import folium
import os
from datetime import datetime


# составляем список файлов GPX в заданной папке
def GPX_Lister(gpx_folder):
    gpx_files = []
    for root, dirs, files in os.walk(gpx_folder, topdown=True):
        for gpx in files:
            _, ending = os.path.splitext(gpx)
            if ending == ".gpx":
                gpx_files.append(os.path.join(root, gpx))
    return gpx_files


gpx_folder = 'C:\\Users\\Rollie\\Documents\\Python Scripts\\Problems\\Germany GPX'
gpx_files = GPX_Lister(gpx_folder)


#  определяем координаты старта и timestamp начала и конца тура
def Time_period(gpx_files):
    total_start_time = 32503669200  # 3000ый год :)
    total_end_time = 0
    for gpx in gpx_files:
        data = open(gpx)
        xmldoc = minidom.parse(data)
        start_point = xmldoc.getElementsByTagName('trkpt')[0]
        date_time = xmldoc.getElementsByTagName('time')
        start_time = date_time[0].firstChild.nodeValue
        end_time = date_time[-1].firstChild.nodeValue
        # преобразуем в unix timestamp
        start_time = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S%z").timestamp()
        end_time = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S%z").timestamp()
        if start_time < total_start_time:
            total_start_time = start_time
            start_coords = (start_point.attributes['lon'].value, start_point.attributes['lat'].value)
        if end_time > total_end_time:
            total_end_time = end_time
    return total_start_time, total_end_time, start_coords


total_start_time, total_end_time, start_coords = Time_period(gpx_files)

# создаем карту Folium на координатах старта тура
myMap = folium.Map(location=[start_coords[1], start_coords[0]], zoom_start=8)


# строим треки и добавляем на карту
def Track_builder(gpx_files):
    color_counter = 0
    for gpx in gpx_files:
        data = open(gpx)
        xmldoc = minidom.parse(data)
        track = xmldoc.getElementsByTagName('trkpt')
        n_track = len(track)
        lon_list = []
        lat_list = []
        for s in range(n_track):
            lon, lat = track[s].attributes['lon'].value, track[s].attributes['lat'].value
            lon_list.append(float(lon))
            lat_list.append(float(lat))
        points = []
        for i in range(len(lon_list)):
            points.append([lat_list[i], lon_list[i]])
        points = points[::4]  # оставляем каждую четвертую точку, чтобы не перегружать HTML
        colors = ["black", "gray", "maroon", "red", "purple", "fuchsia",
                  "green", "lime", "olive", "yellow", "navy", "aqua",
                  "blue", "blueviolet", "brown", "chartreuse", "coral",
                  "cornflowerblue", "crimson", "cyan", "darkblue", "darkcyan",
                  "darkgoldenrod", "darkgreen", "darkkhaki", "darkmagenta",
                  "darkolivegreen", "darkorange", "darkorchid", "darkred",
                  "darksalmon", "darkseagreen", "darkslateblue",
                  "darkslategrey", "darkturquoise", "darkviolet", "deeppink",
                  "deepskyblue", "dimgray", "dimgrey", "dodgerblue",
                  "firebrick", "forestgreen", "fuchsia", "gold", "goldenrod",
                  "gray", "green", "greenyellow", "grey", "hotpink",
                  "indianred", "indigo", "lawngreen", "lightcoral",
                  "lightseagreen", "lightskyblue", "lightslategrey", "lime",
                  "limegreen", "magenta", "maroon", "mediumaquamarine",
                  "mediumblue", "mediumorchid", "mediumpurple",
                  "mediumseagreen", "mediumslateblue", "mediumspringgreen",
                  "mediumturquoise", "mediumvioletred", "midnightblue",
                  "navy", "olive", "olivedrab", "salmon", "sandybrown",
                  "seagreen", "sienna", "skyblue", "slateblue", "slategrey",
                  "springgreen", "steelblue", "tan", "teal", "tomato",
                  "turquoise", "violet", "yellow", "yellowgreen"]
        color = colors[color_counter]
        color_counter += 1
        if color_counter > len(colors):
            color_counter = 0
        folium.PolyLine(points, color=color).add_to(myMap)


Track_builder(gpx_files)


# добавляем на карту лейблы с фотографиями
def Photo_labels(foldername):
    # составляем список JPG
    images = []
    for root, dirs, files in os.walk(foldername, topdown=True):
        for name in files:
            _, ending = os.path.splitext(name)
            if ending == ".jpg":
                images.append(os.path.join(root, name))

    for image in images:
        with open(image, 'rb') as image_file:
            my_image = Image(image_file)

            if my_image.has_exif == False:
                # print("File {} has no EXIF".format(image))
                continue

            try:
                lat_deg = int(my_image.gps_latitude[0])
                lat_min = int(my_image.gps_latitude[1])
                lat_sec = my_image.gps_latitude[2]

                lon_deg = int(my_image.gps_longitude[0])
                lon_min = int(my_image.gps_longitude[1])
                lon_sec = my_image.gps_longitude[2]

                lat_sign = my_image.gps_latitude_ref
                lon_sign = my_image.gps_longitude_ref

                decimal_lat = lat_deg + lat_min/60 + lat_sec/3600
                decimal_lon = lon_deg + lon_min/60 + lon_sec/3600
                photo_width = my_image.pixel_x_dimension
                photo_height = my_image.pixel_y_dimension
            except AttributeError:
                #  print("File {} has no coordinates in EXIF".format(image))
                continue

            if lat_sign == "S":
                decimal_lat *= -1

            if lon_sign == "W":
                decimal_lon *= -1
            photo_time = datetime.strptime(my_image.datetime, "%Y:%m:%d %H:%M:%S").timestamp()
            #  добавить лейбл, если он был сделан во время тура
            if total_end_time > photo_time > total_start_time:
                iframe = '''<html><head><meta name="viewport" content="width=device-width; height=device-height;">
                            <link rel="stylesheet" href="resource://content-accessible/ImageDocument.css">
                            <title>Photo</title></head><body><img src="{}" alt="{}" class="shrinkToFit"
                            width="{}" height="{}"></body></html>'''.format('file:///{}'.format(image).replace("\\", "/"), 'file:///{}'.format(image).replace("\\", "/"), photo_width*0.2, photo_height*0.2)
                popup = folium.Popup(iframe)
                folium.Marker(location=[decimal_lat, decimal_lon], tooltip=iframe,
                                        popup=popup, icon=folium.Icon(color='gray', icon='image', prefix='fa')).add_to(myMap)  # https://fontawesome.com/icons/image


photos_folder = "F:\\Архив\\My Pictures\\2019-07-27 Germany"
Photo_labels(photos_folder)

myMap.save("Germany Tour.html")
print("done!")
