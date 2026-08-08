'''
This script will help you analyze all images in a folder with comprehensive information about each file.

ALTER TABLE pages_catphoto 
ADD COLUMN size INT NULL AFTER photo,
ADD COLUMN SHA256 VARCHAR(64) NULL AFTER size,
ADD COLUMN width INT NULL AFTER SHA256,
ADD COLUMN height INT NULL AFTER width;

'''

import os
import hashlib
from PIL import Image

def get_image_info(folder_path):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in image_extensions):
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                
                file_size = os.path.getsize(file_path)
                
                # Calculate SHA256
                sha256_hash = hashlib.sha256()
                with open(file_path, "rb") as f:
                    sha256_hash.update(f.read())
                
                print(f"Name: {filename}")
                print(f"Size: {file_size} bytes")
                print(f"SHA256: {sha256_hash.hexdigest()}")
                print(f"Width: {width}, Height: {height}")
                print("-" * 50)
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Usage
get_image_info("C:\\Users\\Mike\\Documents\\Python_Scripts\\django-playground\\media\\cat_photos")



'''
ALTER TABLE pages_catphoto 
ADD COLUMN size INT NULL AFTER photo,
ADD COLUMN SHA256 VARCHAR(64) NULL AFTER size,
ADD COLUMN width INT NULL AFTER SHA256,
ADD COLUMN height INT NULL AFTER width;

SET SQL_SAFE_UPDATES = 0;

UPDATE pages_catphoto 
SET size = 25220, 
    SHA256 = '4a90fc9cf182d273c005c438c4793415c4b320f5a183c096a649eaa8fc30fdec', 
    width = 425, 
    height = 268 
WHERE pages_catphoto.photo = 'cat_photos/1.jpg';

UPDATE pages_catphoto 
SET size = 52724, 
    SHA256 = '850ead7615004853f457277f165b5f4153758c21ee228e66f03ce88cfce9faa3', 
    width = 731, 
    height = 533 
WHERE pages_catphoto.photo = 'cat_photos/14117813373971.jpg';

UPDATE pages_catphoto 
SET size = 59787, 
    SHA256 = '4fae35e09144c3a0754ae8fe09dd81d22bdf7a758d0d5194215c0b8556332f50', 
    width = 500, 
    height = 688 
WHERE pages_catphoto.photo = 'cat_photos/14275277146801.jpg';

UPDATE pages_catphoto 
SET size = 51383, 
    SHA256 = '87500d5f03862cca38fe7965ee6e31ab2589a15c5aa2f26a87c74894575258fa', 
    width = 1024, 
    height = 683 
WHERE pages_catphoto.photo = 'cat_photos/1435691453414.jpg';

UPDATE pages_catphoto 
SET size = 150272, 
    SHA256 = '566e76f01bdc1f5e1598f6b3913b780269ef5359d48059dc12a4adb2b51143a5', 
    width = 560, 
    height = 754 
WHERE pages_catphoto.photo = 'cat_photos/1435692082209.jpg';

UPDATE pages_catphoto 
SET size = 99631, 
    SHA256 = '4cd2a93a271a5f3a6f57a87dd174ce7e1dfbcc3cd707e95e5c99a1cc3b2375e3', 
    width = 1024, 
    height = 768 
WHERE pages_catphoto.photo = 'cat_photos/1435692148733.jpg';

UPDATE pages_catphoto 
SET size = 39353, 
    SHA256 = '3fce97a74620ff315f515408346a36ef7b823aee0a32f1a189bdbf92c3f19ff0', 
    width = 500, 
    height = 376 
WHERE pages_catphoto.photo = 'cat_photos/1435694078613.jpg';

UPDATE pages_catphoto 
SET size = 72990, 
    SHA256 = 'ee827f4eb5b2e37f69a5c387c6e2aad5a80ee68e47afd269b26de6d017088744', 
    width = 807, 
    height = 645 
WHERE pages_catphoto.photo = 'cat_photos/14662200939630.jpg';

UPDATE pages_catphoto 
SET size = 110232, 
    SHA256 = '3b0070c55b688033e087c4bf81f70f15e12fa447b6fc992dca821ae80a01ac36', 
    width = 800, 
    height = 600 
WHERE pages_catphoto.photo = 'cat_photos/14662208180752.jpg';

UPDATE pages_catphoto 
SET size = 1749739, 
    SHA256 = 'e2db9d727b2a344bf9cf1d88795dacf2de847aac464a59bf1cfa370bf5de2b35', 
    width = 2000, 
    height = 1328 
WHERE pages_catphoto.photo = 'cat_photos/1589711817049.jpg';

UPDATE pages_catphoto 
SET size = 41543, 
    SHA256 = '0713d4884382398ee4e98e7826109f64c669f7b3e55c3baf6a2c2d477f55453d', 
    width = 440, 
    height = 309 
WHERE pages_catphoto.photo = 'cat_photos/2.jpg';

UPDATE pages_catphoto 
SET size = 36290, 
    SHA256 = '2f220b3d1314484870152fe0fc923dd9ca2309aad7b8b553668a5cdea52483e1', 
    width = 435, 
    height = 259 
WHERE pages_catphoto.photo = 'cat_photos/3.jpg';

UPDATE pages_catphoto 
SET size = 53761, 
    SHA256 = 'aa4dc28a2f6baf8a9415026186e29212550c2cc6cfbbf4ffcde453947342ac3b', 
    width = 440, 
    height = 440 
WHERE pages_catphoto.photo = 'cat_photos/4.jpg';

UPDATE pages_catphoto 
SET size = 52059, 
    SHA256 = '21ba6c14c387a7e1fa61c74a350061176e41a88b600eefc3348fa77c368427b2', 
    width = 440, 
    height = 440 
WHERE pages_catphoto.photo = 'cat_photos/5.jpg';

UPDATE pages_catphoto 
SET size = 38197, 
    SHA256 = '8691734c3dbaad99e25b0a5cf617cf7f8999c5d5c0cf35328116c5388bc9b5db', 
    width = 440, 
    height = 440 
WHERE pages_catphoto.photo = 'cat_photos/6.jpg';

UPDATE pages_catphoto 
SET size = 52358, 
    SHA256 = '30023c46e86b0090e1b857dfb0ec4ec45a8cf8d85d9f418d5f4795cb06e3a5b1', 
    width = 440, 
    height = 330 
WHERE pages_catphoto.photo = 'cat_photos/7.jpg';

UPDATE pages_catphoto 
SET size = 23765, 
    SHA256 = '055085534ae3f47f61cd8af8d7e77fc0ecb15b893aceae6c8b8dbcc89bcdc0ad', 
    width = 421, 
    height = 405 
WHERE pages_catphoto.photo = 'cat_photos/8.jpg';

UPDATE pages_catphoto 
SET size = 49675, 
    SHA256 = 'f689dd602a87076a2b64818939ce57b6652eb1623e15dfa86afdddca4be60f95', 
    width = 440, 
    height = 421 
WHERE pages_catphoto.photo = 'cat_photos/9.jpg';

UPDATE pages_catphoto 
SET size = 28859, 
    SHA256 = '1f3a2b5e9e7c7978291def67ea261dd7816ab973e31615604f371faab23fce78', 
    width = 440, 
    height = 330 
WHERE pages_catphoto.photo = 'cat_photos/90.jpg';

UPDATE pages_catphoto 
SET size = 21394, 
    SHA256 = '3d32a99c8ee4491c12a89332537d7e0c947db5d59dc9fb1fc71769a7b13d10b9', 
    width = 400, 
    height = 400 
WHERE pages_catphoto.photo = 'cat_photos/91.jpg';

UPDATE pages_catphoto 
SET size = 44657, 
    SHA256 = 'c6dceb735a0cfe9feca469b10bfdc87ecfc46be8e7f99446324f9bcd03000361', 
    width = 440, 
    height = 440 
WHERE pages_catphoto.photo = 'cat_photos/a7c49da7gw1ey0x52qkjqj20c80c8jsb.jpg';

UPDATE pages_catphoto 
SET size = 51229, 
    SHA256 = '2e6a953b3df7404cd151740cf7fa58d0cfef6e029088622cf898395e1ef8c9c8', 
    width = 440, 
    height = 440 
WHERE pages_catphoto.photo = 'cat_photos/a7c49da7gw1ey0x539760j20c80c80tu.jpg';

UPDATE pages_catphoto 
SET size = 45241, 
    SHA256 = 'd11bd2ae63968d0e76a37ff7cba089b977b0dd6b48815bda7f728932f1ba2927', 
    width = 440, 
    height = 326 
WHERE pages_catphoto.photo = 'cat_photos/a7c49da7jw1ejsrjhl7fpj20c80923zg.jpg';

UPDATE pages_catphoto 
SET size = 48770, 
    SHA256 = '23b96da42a59b7b728d7b5ae312c7d7b9178db328dd404180052e7e197be3f2c', 
    width = 440, 
    height = 771 
WHERE pages_catphoto.photo = 'cat_photos/a7c49da7jw1ejsrjq4cr7j20c80lfjsf.jpg';

UPDATE pages_catphoto 
SET size = 29786, 
    SHA256 = '94559602bcb8736c0742a70dfeeb282b8d3eb15bd335644f44417498467b5c7b', 
    width = 440, 
    height = 330 
WHERE pages_catphoto.photo = 'cat_photos/a7c49da7jw1ejsrjunmgfj20c80960t9.jpg';

UPDATE pages_catphoto 
SET size = 50145, 
    SHA256 = '18d1967ac0dc6508d99bd4a53787ea99e142dbb298656b38311c00bf6c215af9', 
    width = 440, 
    height = 330 
WHERE pages_catphoto.photo = 'cat_photos/a7c49da7jw1ejsrjwrzpij20c8096wfk.jpg';

UPDATE pages_catphoto 
SET size = 169948, 
    SHA256 = '12c8dbcfb0d6d3353d1edb57aaad5f70359eb5c3327fe0cdba2d25cc0f563060', 
    width = 500, 
    height = 574 
WHERE pages_catphoto.photo = 'cat_photos/jellybeans.jpg';

UPDATE pages_catphoto 
SET size = 37782, 
    SHA256 = '6d0667ad413c23c049c9bf168e39603fa08def1f0f62aab3f950d5b33d692bbe', 
    width = 500, 
    height = 375 
WHERE pages_catphoto.photo = 'cat_photos/z1352737299038.jpg';
'''