# https://cloudinary.com/documentation/django_integration
# https://cloudinary.com/documentation/image_upload_api_reference
# https://cloudinary.com/documentation/admin_api#get_resources

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "dq0j8nvsz", 
  api_key = "429268596266338", 
  api_secret = "fgzjSTei_Uevjc77AGwt8X0-JXI" 
)

# cloudinary.uploader.upload("C:\\Users\\TN90072\\Pictures\\My Post-1.jpg", 
#   folder = "Germany", 
#   #public_id = "APIied",
#   overwrite = 'true', 
#   use_filename = 'true',
#   unique_filename = 'false',
#   #notification_url = "https://mysite.example.com/notify_endpoint", 
#   resource_type = "image")


folder_response  = cloudinary.api.resources(type = "upload", prefix = "Germany")
for photo in folder_response["resources"]:
  print(photo["url"])