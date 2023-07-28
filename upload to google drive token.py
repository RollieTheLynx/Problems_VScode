'''
Desktop app auth
Авторизуемся один раз, потом сохраняется файл token.json
Здесь API v3

https://developers.google.com/drive/api/guides/manage-uploads

Credentials of my app:
https://console.cloud.google.com/apis/credentials?project=python-uploader-391919

'''

import os.path
import io
import mimetypes

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleapiclient.http


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def authorize():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
    return service


def insert_a_file(drive_service, FILENAME, TITLE, DESCRIPTION, parent_id = '1GaC5q885w03hg3iGoU-oYbseg_adTq2D'):
    """Insert a file. Files are comprised of contents and metadata.
    MediaFileUpload abstracts uploading file contents from a file on disk.
    Args:
        drive_service: authorization thing
        FILENAME: absolute path to file
        TITLE: how it's called in Drive, must have extension
        DESCRIPTION: text description
        parent_id: id of parent folder
    Returns:
        None"""
    
    media_body = googleapiclient.http.MediaFileUpload(
        FILENAME,
        mimetype=mimetypes.MimeTypes().guess_type(FILENAME)[0],
        resumable=True
    )
    # The body contains the metadata for the file.
    body = {
        'name': TITLE,
        'description': DESCRIPTION,
        "parents" : [parent_id]
    }

    # Perform the request and print the result.
    try:
        new_file = drive_service.files().create(
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
    # folderid is the 1Ga.. part in its link: https://drive.google.com/drive/folders/1GaC5q885w03hg3iGoU-oYbseg_adTq2D
    body = {
        'name': folderName,
        'mimeType': "application/vnd.google-apps.folder",
        'description': 'Folder created with python'
    }
    if parentID:
        body['parents'] = [parentID]
        root_folder = drive_service.files().create(body = body).execute()
    return root_folder['id']


def uploadFolder(service, folder_path, parents_id):
    """Upload folder with all files and subfolders
    Args:
        drive_service: authorization thing
        folder_path: absolute path to the folder, must have (double) slash in the end
        parents_id: id of parent folder
    Returns:
        None"""
    
    # сначала загружаем файлы
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            print(item)
            insert_a_file(service, os.path.join(folder_path, item), item, '', parent_id = parents_id)
            print(f"Inserted file {item} to id {parents_id}")

    # потом рекурсивно загружаем подпапки
    for item in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, item)):
            print(item)
            parents_id = create_folder(service, item, parents_id)
            print(f'Created folder {item} with id {parents_id}')
            print(f"Uploading folder {os.path.join(folder_path, item)}")
            uploadFolder(service, os.path.join(folder_path, item), parents_id)


def download_file(drive_service, file_id):
    """Downloads a single file
    Args:
        drive_service: authorization thing
        file_id: ID of the file to download
    Returns:
        None
    """
    try:
        file_metadata = drive_service.files().get(fileId=file_id).execute()
        if file_metadata['mimeType'] == 'application/vnd.google-apps.folder':
            print('Is folder. Feed me file IDs!')
            # getIdsInFolder(file_id)
        else:
            # all metadata: https://developers.google.com/drive/api/reference/rest/v3/files
            request = drive_service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = googleapiclient.http.MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(F'Download {int(status.progress() * 100)}.')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    filename = file_metadata['name']
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(file.getbuffer())

    # return file.getvalue()  # IO object with location.

def download_files(service, folder_id, output_dir):
    page_token = None
    while True:
        response = service.files().list(
            q=f"'{folder_id}' in parents",
            spaces='drive',
            fields='nextPageToken, files(id, name, mimeType)',
            pageToken=page_token
        ).execute()

        for file in response.get('files', []):
            file_id = file['id']
            file_name = file['name']
            mime_type = file['mimeType']
            
            if mime_type == 'application/vnd.google-apps.folder':
                # If the file is a subfolder, recursively call the function to download its contents.
                subfolder = os.path.join(output_dir, file_name)
                if not os.path.exists(subfolder):
                    os.makedirs(subfolder)
                download_files(service, file_id, subfolder)
            else:
                # If the file is not a folder, download it.
                request = service.files().get_media(fileId=file_id)
                file_path = os.path.join(output_dir, file_name)
                with open(file_path, 'wb') as f:
                    f.write(request.execute())
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

service = authorize()

# new_folder_id = create_folder(service, "Subfolder 88", '1GaC5q885w03hg3iGoU-oYbseg_adTq2D')
# insert_a_file(service, 'screenie_bin.jpg', 'screenie_bin.jpg', 'A shiny new image', new_folder_id)
# insert_a_file(service, 'C:\\Users\\Mike\\Desktop\\Copy of Таблица поиска.xlsx', 'Copy of Таблица поиска.xlsx', 'A shiny new image', new_folder_id)

# upload_files_infolder('C:\\Users\\Mike\\Desktop\\temp\\')
# download_file('1Fo_MoZvrDJrL74PIkvzLdP1qt46EdsBB') # pdf


# # Download entire folder with subfolders:
# output_dir = 'test download'
# if not os.path.exists(output_dir):
#    os.makedirs(output_dir)
# download_files(service, '1GaC5q885w03hg3iGoU-oYbseg_adTq2D', output_dir)


# Upload entire folder with subfolders:
folder_path = 'C:\\Users\\Mike\\Desktop\\temp\\'
folderName = os.path.basename(os.path.dirname(folder_path))
parents_id = create_folder(service, folderName, parentID = '1GaC5q885w03hg3iGoU-oYbseg_adTq2D')
uploadFolder(service, folder_path, parents_id)