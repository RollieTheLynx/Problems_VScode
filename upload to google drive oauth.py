'''
OAuth authorization https://developers.google.com/workspace/guides/create-credentials#api-key 
Каждый раз авторизуемся в аккаунт
Здесь API v2

https://developers.google.com/drive/api/guides/manage-uploads

Credentials of my app:
https://console.cloud.google.com/apis/credentials?project=python-uploader-391919

'''


import googleapiclient.http
import httplib2
import oauth2client.client
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import mimetypes
import os

# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.
OAUTH2_SCOPE = 'https://www.googleapis.com/auth/drive'

# Location of the client secrets.
CLIENT_SECRETS = 'credentials.json'

def authorize():
    # Perform OAuth2.0 authorization flow.
    flow = oauth2client.client.flow_from_clientsecrets(
        CLIENT_SECRETS, OAUTH2_SCOPE)
    flow.redirect_uri = oauth2client.client.OOB_CALLBACK_URN
    authorize_url = flow.step1_get_authorize_url()
    print('Go to the following link in your browser: ' + authorize_url)
    # `six` library supports Python2 and Python3 without redefining builtin input()
    code = input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)

    # Create an authorized Drive API client.
    http = httplib2.Http()
    credentials.authorize(http)
    drive_service = build('drive', 'v2', http=http)
    return drive_service

def insert_a_file(FILENAME, MIMETYPE, TITLE, DESCRIPTION, drive_service, parent_id = '1GaC5q885w03hg3iGoU-oYbseg_adTq2D'):
 
    # Insert a file. Files are comprised of contents and metadata.
    # MediaFileUpload abstracts uploading file contents from a file on disk.
    media_body = googleapiclient.http.MediaFileUpload(
        FILENAME,
        mimetype=MIMETYPE,
        resumable=True
    )
    # The body contains the metadata for the file.
    body = {
        'title': TITLE,
        'description': DESCRIPTION,
        "parents" : [{'id': parent_id}]
    }

    # Perform the request and print the result.
    try:
        new_file = drive_service.files().insert(
            body=body, media_body=media_body).execute()
        file_title = new_file.get('title')
        file_desc = new_file.get('description')
        if file_title == TITLE and file_desc == DESCRIPTION:
            print(f"File is uploaded \nTitle : {file_title}  \nDescription : {file_desc}")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


def create_folder(drive_service, folderName, parentID = None):
    # Create a folder on Drive, returns the newely created folders ID
    # folderid is last part in its link: https://drive.google.com/drive/folders/1GaC5q885w03hg3iGoU-oYbseg_adTq2D
    body = {
        'title': folderName,
        'mimeType': "application/vnd.google-apps.folder",
        'description': 'Folder created with python'
    }
    if parentID:
        body['parents'] = [{'id': parentID}]
    root_folder = drive_service.files().insert(body = body).execute()
    return root_folder['id']

def upload_files_infolder(folder_path):
    # list to store files
    file_data = []
    # Iterate directory
    for path in os.listdir(folder_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(folder_path, path)):
            mime_type = mimetypes.MimeTypes().guess_type(path)[0]
            title = os.path.splitext(path)[0]
            description = ''
            file_data.append([os.path.join(folder_path, path), mime_type, title, description])
    print(file_data)

    drive_service = authorize()
    for file in file_data:
        insert_a_file(file[0], file[1], file[2], file[3], drive_service, parent_id = '1GaC5q885w03hg3iGoU-oYbseg_adTq2D')



if __name__ == '__main__':
    # drive_service = authorize()
    # new_folder_id = create_folder(drive_service, "Subfolder 1", '1GaC5q885w03hg3iGoU-oYbseg_adTq2D')
    # insert_a_file('screenie_bin.jpg', 'image/jpeg', 'screenie_bin', 'A shiny new image', drive_service, new_folder_id)
    upload_files_infolder('C:\\Users\\Mike\\Desktop\\temp\\')

    #TODO guess mime of xlsx