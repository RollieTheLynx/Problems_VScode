'''
Считывает файлы GPX и фотографии с геометками и создает HTML с вашмим туром!
'''
from xml.dom import minidom
from exif import Image
import folium
import os
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api

# TODO добавить считывание из локального файла
cloudinary.config( 
  cloud_name = "dq0j8nvsz", 
  api_key = "429268596266338", 
  api_secret = "fgzjSTei_Uevjc77AGwt8X0-JXI" 
)

# составляем список файлов с нужным расширением в заданной папке
def File_Lister(folder, extension):
    files_list = []
    for root, dirs, files in os.walk(folder, topdown=True):
        for gpx in files:
            _, ending = os.path.splitext(gpx)
            if ending == extension:
                files_list.append(os.path.join(root, gpx))
    return files_list


#gpx_folder = 'C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\Germany GPX'
gpx_folder = 'C:\\Users\\Rollie\\Documents\\Python_Scripts\\Problems_VScode\\Estonia GPX'
gpx_files = File_Lister(gpx_folder, ".gpx")

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
        colors = ["black", "maroon", "red", "purple", "fuchsia",
                  "green", "lime", "olive", "yellow", "navy", "aqua",
                  "blue", "blueviolet", "brown", "chartreuse", "coral",
                  "crimson", "cyan", "darkblue", "darkcyan",
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


# загружаем фотки в облако
def UploadFolder2Cloudinary(foldername):
    images = File_Lister(foldername, ".jpg")
    for image in images:
        cloudinary.uploader.upload(image, 
        folder = foldername.split("\\")[-1], 
        overwrite = 'true', 
        use_filename = 'true',
        unique_filename = 'false',
        resource_type = "image")
photos_folder = "F:\\Архив\\My Pictures\\2018-07-14 Эстония"
UploadFolder2Cloudinary(photos_folder)

# получаем ссылки на файлы из облака и сопоставляем с локальными файлами в словаре
folder_response  = cloudinary.api.resources(type = "upload", prefix = "Germany") # prefix = имя папки на cloudinary
file_dictionary = {}
for photo in folder_response["resources"]:
  file_dictionary[photo["url"].split("/")[-1]] = photo["url"]
print(file_dictionary)


# добавляем на карту лейблы с фотографиями
def Photo_labels(foldername):
    # составляем список JPG
    images = File_Lister(foldername, ".jpg")
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
                # file_link = 'file:///{}'.format(image).replace("\\", "/") # для локальных фалов на компе
                file_link = file_dictionary[image].replace("\\", "/")
                # ссылка вида http://res.cloudinary.com/dq0j8nvsz/image/upload/v1621842090/Germany/1604545559682_wrxs6h.jpg
                thumb_link = file_link.split('/')[0:6] + ['c_thumb,w_{},h_{},g_face'.format(photo_width*0.2, photo_height*0.2)] + file_link.split('/')[6:9].join("/")
                # thumb вида https://res.cloudinary.com/dq0j8nvsz/image/upload/c_thumb,w_200,g_face/v1621842090/Germany/1604545559682_wrxs6h.jpg
                # https://cloudinary.com/documentation/transformation_reference
                iframe = '''<html>
                                <head>
                                    <meta name="viewport" content="width=device-width; height=device-height;">
                                    <link rel="stylesheet" href="resource://content-accessible/ImageDocument.css">
                                    <title>
                                        Photo
                                    </title>
                                </head>
                                <body>
                                    <a href="{}" target="_blank">
                                        <img src="{}" alt="{}" class="shrinkToFit" width="{}" height="{}">
                                    </a>
                                </body>
                            </html>'''.format(file_link, thumb_link, file_link, photo_width*0.2, photo_height*0.2)
                popup = folium.Popup(iframe)
                folium.Marker(location=[decimal_lat, decimal_lon], tooltip=iframe,
                              popup=popup, icon=folium.Icon(color='gray', icon='image', prefix='fa')).add_to(myMap)  # https://fontawesome.com/icons/image


#photos_folder = "F:\\Архив\\My Pictures\\2019-07-27 Germany"
photos_folder = "F:\\Архив\\My Pictures\\2018-07-14 Эстония"
Photo_labels(photos_folder)

myMap.save("Estonia Tour.html")
print("Done!")